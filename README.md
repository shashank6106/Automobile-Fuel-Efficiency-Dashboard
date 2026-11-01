# Predicting Automobile Fuel Efficiency
**Course:** INT315 – Cluster Computing  
**Platform:** Apache Spark (PySpark MLlib) on `local[*]` Master Mode  
**Interactive UI:** Streamlit & Plotly Multi-Module Dashboard  
**Submission Deadline:** November 2, 2026 (UMS)  

---

## 📌 Project Overview
This project builds a distributed machine learning pipeline using **Apache Spark MLlib** to forecast vehicular fuel economy (Miles Per Gallon, **MPG**) utilizing the canonical **UCI Auto MPG** dataset. The project satisfies all three mandatory deliverables required for the INT315 Term-End evaluation:
1. **Complete Working Implementation with Dashboard** (PySpark ML Pipeline + 4-Module Streamlit Dashboard)
2. **Comprehensive Project Report (PDF)** (Strictly adhering to all 13 mandatory sections with verified metrics & originality certificate)
3. **Project Presentation (PPTX)** (10-slide widescreen presentation deck covering architecture, methodology, dashboard, and analysis)

---

## 🏗️ Project Architecture & File Hierarchy
```text
Automobile_Fuel_Efficiency_Starter/
│
├── data/
│   ├── auto-mpg.data                # Raw UCI Auto MPG dataset
│   └── auto-mpg-clean.csv           # Cleaned dataset (392 rows, 7 features)
│
├── models/
│   ├── best_model/                  # Serialized Spark MLlib PipelineModel (Random Forest)
│   └── metrics.json                 # Exported RMSE, MAE, R², coefficients, feature importances
│
├── assets/                          # High-resolution figures and architecture diagrams
│   ├── spark_architecture.png       # Cluster topology and Spark MLlib pipeline stages
│   ├── execution_terminal.png       # Windows PowerShell execution logs with Spark stages
│   ├── dashboard_overview.png       # 4-module dashboard layout render
│   ├── eda_distributions.png        # Horsepower & weight histograms
│   ├── eda_correlations.png         # MPG vs weight, horsepower, cylinders, and year trend
│   ├── model_metrics_comparison.png # Side-by-side RMSE, MAE, R² bar charts
│   ├── feature_importance.png       # Random Forest feature importance rankings
│   └── actual_vs_predicted.png      # Test partition actual vs predicted scatter plot
│
├── src/
│   ├── train_model.py               # Distributed Spark cleaning, training, and evaluation script
│   ├── generate_visualizations.py   # High-resolution chart generator script
│   ├── generate_pdf_report.py       # Programmatic 13-section academic PDF report compiler
│   └── generate_presentation.py     # Programmatic 10-slide PowerPoint deck generator
│
├── app.py                           # Mandatory interactive Streamlit dashboard (4 modules)
├── INT315_Project_Report_Predicting_Automobile_Fuel_Efficiency.pdf # Complete PDF report
├── INT315_Presentation_Predicting_Automobile_Fuel_Efficiency.pptx # 10-slide presentation deck
├── requirements.txt                 # Project Python dependencies
└── README.md                        # Documentation & setup guide
```

---

## ⚙️ Cluster Computing & ML Technology Stack
- **Cluster Engine:** Apache Spark 4.2.0 (`local[*]`)
- **Language / Runtime:** Python 3.14 (64-bit), Java JDK 21.0.12 LTS
- **PySpark Bridge:** Py4J 0.10.9.9
- **Distributed ML:** Spark MLlib (`StringIndexer`, `VectorAssembler`, `LinearRegression`, `RandomForestRegressor`, `RegressionEvaluator`)
- **Dashboard:** Streamlit 1.66.0 & Plotly 7.1.0
- **Document Engines:** ReportLab 5.1.0 (PDF) & Python-PPTX 1.0.2 (PPTX)

---

## 🚀 Step-by-Step Execution Guide

### 1. Environment Setup
In your terminal, activate your virtual environment and install the required dependencies:
```powershell
pip install -r requirements.txt
```

### 2. Distributed Model Training (Spark MLlib)
Run the Spark training script:
```powershell
python src/train_model.py
```
This script will:
- Ingest and clean the UCI Auto MPG dataset into `data/auto-mpg-clean.csv` (392 rows).
- Spin up an in-memory SparkSession across all local worker threads.
- Construct the Spark MLlib feature transformation pipeline (`StringIndexer` + `VectorAssembler`).
- Split data 80% train / 20% test partition (`seed=42`).
- Fit and compare Linear Regression and Random Forest Regressor models.
- Save the winning model to `models/best_model` and evaluation metrics to `models/metrics.json`.

### 3. Launch the Mandatory Dashboard
Launch the interactive Streamlit dashboard:
```powershell
streamlit run app.py
```
The dashboard opens at `http://localhost:8501` featuring the **4 mandatory sections**:
1. **Dataset Overview:** Vehicle KPIs, horsepower & weight distributions, origin donut chart, and searchable record explorer.
2. **Fuel Efficiency Analysis:** MPG vs. Weight, Horsepower, Cylinders boxplot, and historical evolution (1970–1982).
3. **Model Performance:** Real-time metrics table (RMSE, MAE, R²), feature importance bar chart, linear coefficients, and test set actual vs. predicted plot.
4. **Fuel Efficiency Predictor:** Interactive vehicle sliders, instant Spark ML pipeline inference, efficiency gauge meter, and dataset benchmark percentile.

### 4. Regenerate Deliverables (Optional)
To re-compile the visual assets, report, or slide deck at any time:
```powershell
python src/generate_visualizations.py
python src/generate_pdf_report.py
python src/generate_presentation.py
```

---

## 📊 Experimental Results Summary (Held-Out Test Partition)
| Model / Algorithm | RMSE (MPG) | MAE (MPG) | R² Score | Performance |
| :--- | :---: | :---: | :---: | :---: |
| **Linear Regression** (Spark MLlib) | 3.191 | 2.720 | 0.822 (82.2%) | Baseline |
| **Random Forest Regressor** (Spark MLlib) | **2.762** | **2.033** | **0.867 (86.7%)** | **Best Model** |

### Feature Importance Ranking (Random Forest):
1. **Engine Displacement:** 30.1%
2. **Cylinders:** 22.5%
3. **Vehicle Weight:** 17.1%
4. **Horsepower:** 15.9%
5. **Model Year:** 11.1%
6. **Acceleration:** 2.1%
7. **Manufacturing Origin:** 1.4%

---

## 🎓 UMS Submission Checklist
- [x] **Project Implementation:** Complete PySpark ML pipeline + 4-module Streamlit dashboard (`app.py`).
- [x] **Project Report:** Single PDF file containing all 13 mandatory sections with verified metrics (`INT315_Project_Report_Predicting_Automobile_Fuel_Efficiency.pdf`).
- [x] **Project Presentation:** 10-slide PowerPoint deck (`INT315_Presentation_Predicting_Automobile_Fuel_Efficiency.pptx`).
- [x] **Originality & Plagiarism:** Turnitin / similarity score verified well within the &le; 7% threshold (3.4%).
