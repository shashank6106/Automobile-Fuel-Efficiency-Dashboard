import os
import json
import urllib.request
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.regression import LinearRegression, RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT, "data")
MODEL_DIR = os.path.join(ROOT, "models")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
RAW_PATH = os.path.join(DATA_DIR, "auto-mpg.data")
CLEAN_PATH = os.path.join(DATA_DIR, "auto-mpg-clean.csv")

COLUMNS = [
    "mpg", "cylinders", "displacement", "horsepower", "weight",
    "acceleration", "model_year", "origin", "car_name"
]
FEATURES = [
    "cylinders", "displacement", "horsepower", "weight",
    "acceleration", "model_year", "origin"
]

def download_and_clean():
    if not os.path.exists(RAW_PATH):
        print("Downloading UCI Auto MPG dataset...")
        urllib.request.urlretrieve(DATA_URL, RAW_PATH)

    # Parse robustly by taking first 8 fields and the remainder as car_name
    rows = []
    with open(RAW_PATH, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 9:
                continue
            car_name = " ".join(parts[8:]).strip('"')
            rows.append(parts[:8] + [car_name])
    df = pd.DataFrame(rows, columns=COLUMNS)
    for c in COLUMNS[:8]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=COLUMNS[:8]).copy()
    df["origin"] = df["origin"].astype(int).astype(str)
    df.to_csv(CLEAN_PATH, index=False)
    print(f"Cleaned dataset saved: {CLEAN_PATH}")
    print(f"Rows after cleaning: {len(df)}")
    return df

def main():
    pdf = download_and_clean()
    spark = (
        SparkSession.builder
        .appName("AutomobileFuelEfficiency")
        .master("local[*]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    sdf = spark.read.csv(CLEAN_PATH, header=True, inferSchema=True)
    sdf = sdf.withColumn("origin", col("origin").cast("string"))

    indexer = StringIndexer(inputCol="origin", outputCol="origin_index", handleInvalid="keep")
    feature_cols = [c for c in FEATURES if c != "origin"] + ["origin_index"]
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")

    train, test = sdf.randomSplit([0.8, 0.2], seed=42)
    evaluator_rmse = RegressionEvaluator(labelCol="mpg", predictionCol="prediction", metricName="rmse")
    evaluator_mae = RegressionEvaluator(labelCol="mpg", predictionCol="prediction", metricName="mae")
    evaluator_r2 = RegressionEvaluator(labelCol="mpg", predictionCol="prediction", metricName="r2")

    results = {}
    details = {}
    best_name, best_rmse, best_model = None, float("inf"), None

    models = [
        ("Linear Regression", LinearRegression(featuresCol="features", labelCol="mpg", maxIter=100)),
        ("Random Forest", RandomForestRegressor(featuresCol="features", labelCol="mpg", numTrees=100, seed=42))
    ]

    for name, estimator in models:
        pipeline = Pipeline(stages=[indexer, assembler, estimator])
        fitted = pipeline.fit(train)
        predictions = fitted.transform(test)
        rmse = evaluator_rmse.evaluate(predictions)
        mae = evaluator_mae.evaluate(predictions)
        r2 = evaluator_r2.evaluate(predictions)
        results[name] = {"RMSE": rmse, "MAE": mae, "R2": r2}
        print(f"{name}: RMSE={rmse:.3f}, MAE={mae:.3f}, R2={r2:.3f}")
        
        # Save model details (coefficients or feature importances)
        model_stage = fitted.stages[2]
        if hasattr(model_stage, "featureImportances"):
            details[name] = {
                "type": "RandomForest",
                "feature_importances": dict(zip(feature_cols, [float(x) for x in model_stage.featureImportances.toArray()]))
            }
        elif hasattr(model_stage, "coefficients"):
            details[name] = {
                "type": "LinearRegression",
                "intercept": float(model_stage.intercept),
                "coefficients": dict(zip(feature_cols, [float(x) for x in model_stage.coefficients.toArray()]))
            }

        # Collect predictions for visualization
        pred_sample = predictions.select("mpg", "prediction", "car_name").toPandas().to_dict(orient="records")
        details[name]["sample_predictions"] = pred_sample[:50]

        if rmse < best_rmse:
            best_name, best_rmse, best_model = name, rmse, fitted

    best_model_path = os.path.join(MODEL_DIR, "best_model")
    if os.path.exists(best_model_path):
        import shutil
        shutil.rmtree(best_model_path)
    best_model.write().overwrite().save(best_model_path)

    metrics_payload = {
        "models": results,
        "details": details,
        "best_model": best_name,
        "features": feature_cols,
        "train_rows": train.count(),
        "test_rows": test.count()
    }

    with open(os.path.join(MODEL_DIR, "metrics.json"), "w") as f:
        json.dump(metrics_payload, f, indent=2)

    print(f"\nBest model: {best_name}")
    print(f"Saved model to: {best_model_path}")
    print("Training complete.")
    spark.stop()

if __name__ == "__main__":
    main()
