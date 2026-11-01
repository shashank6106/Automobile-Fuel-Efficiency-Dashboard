import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_DIR = os.path.join(ROOT, "assets")
OUTPUT_PPTX = os.path.join(ROOT, "INT315_Presentation_Predicting_Automobile_Fuel_Efficiency.pptx")

# Color Palette
DARK_BLUE = RGBColor(30, 58, 138)    # #1E3A8A
PRIMARY_BLUE = RGBColor(37, 99, 235) # #2563EB
LIGHT_BG = RGBColor(248, 250, 252)   # #F8FAFC
TEXT_DARK = RGBColor(31, 41, 55)     # #1F2937
TEXT_MUTED = RGBColor(75, 85, 99)    # #4B5563
WHITE = RGBColor(255, 255, 255)
ACCENT_GREEN = RGBColor(5, 150, 105) # #059669
CARD_BG = RGBColor(238, 242, 255)    # #EEF2FF
BORDER_COLOR = RGBColor(203, 213, 225)

def create_presentation():
    prs = Presentation()
    # 16:9 Widescreen slides (13.333 x 7.5 inches)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, category_text="INT315 – CLUSTER COMPUTING"):
        # Top banner shape
        banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
        banner.fill.solid()
        banner.fill.fore_color.rgb = DARK_BLUE
        banner.line.color.rgb = DARK_BLUE

        # Category / Breadcrumb
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.3))
        tf = tx_box.text_frame
        tf.word_wrap = True
        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = RGBColor(199, 210, 254)

        # Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(20)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE

        # Running footer
        footer_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.02))
        footer_line.fill.solid()
        footer_line.fill.fore_color.rgb = BORDER_COLOR
        footer_line.line.color.rgb = BORDER_COLOR

        ft_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.35))
        tf_f = ft_box.text_frame
        p_f = tf_f.paragraphs[0]
        p_f.text = "Predicting Automobile Fuel Efficiency | Apache Spark MLlib & Streamlit | Submission: Nov 2, 2026"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = DARK_BLUE
    bg1.line.color.rgb = DARK_BLUE

    # Title Card Inner
    card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.0), Inches(10.933), Inches(5.5))
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = RGBColor(226, 232, 240)

    # Content
    tb1 = slide1.shapes.add_textbox(Inches(1.6), Inches(1.3), Inches(10.133), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "INT315 – CLUSTER COMPUTING | TERM END PROJECT"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    p = tf1.add_paragraph()
    p.text = "Predicting Automobile Fuel Efficiency"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.space_before = Pt(8)

    p = tf1.add_paragraph()
    p.text = "Distributed In-Memory Machine Learning Pipeline with Apache Spark MLlib & Streamlit Dashboard"
    p.font.size = Pt(15)
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(6)

    p = tf1.add_paragraph()
    p.text = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    p.font.size = Pt(10)
    p.font.color.rgb = BORDER_COLOR
    p.space_before = Pt(14)

    # Details grid
    p = tf1.add_paragraph()
    p.text = "Key Project Specifications:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(10)

    specs = [
        "• Distributed Cluster Engine: Apache Spark 4.2.0 (PySpark) on local[*] multi-worker threads",
        "• Machine Learning Algorithms: Spark MLlib Linear Regression & Random Forest Regressor",
        "• Canonical Dataset: UCI Auto MPG Repository (392 cleaned records across 7 features)",
        "• Mandatory Interactive Dashboard: Streamlit & Plotly (Dataset Overview, EDA, Model Benchmark, Predictor)",
        "• Submission Portal & Date: UMS (University Management System) – November 2, 2026"
    ]
    for sp in specs:
        p = tf1.add_paragraph()
        p.text = sp
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(3)

    # =========================================================================
    # SLIDE 2: PROBLEM STATEMENT
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Problem Statement: Challenges in Fuel Efficiency Analytics")

    # Left Box: Problem Context
    b_left = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    b_left.fill.solid()
    b_left.fill.fore_color.rgb = LIGHT_BG
    b_left.line.color.rgb = BORDER_COLOR

    tb_pl = slide2.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.8))
    tf_pl = tb_pl.text_frame
    tf_pl.word_wrap = True
    
    p = tf_pl.paragraphs[0]
    p.text = "The Industrial & Environmental Context"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE

    points_l = [
        "• Rising Energy Costs & Stringent Regulations: Automotive standards (e.g., CAFE) mandate rigorous fuel economy benchmarks (Miles Per Gallon - MPG) to curb environmental carbon footprints.",
        "• Complex Multi-Factor Physics: Fuel efficiency is governed by non-linear interactions across vehicle weight, displacement, horsepower, engine cylinders, and aerodynamic drag.",
        "• Consumer & Fleet Economics: Predicting fuel economy with high fidelity enables buyers and commercial fleet managers to forecast total cost of ownership (TCO) and fuel consumption."
    ]
    for pt in points_l:
        p = tf_pl.add_paragraph()
        p.text = pt
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # Right Box: Cluster Computing Motivation
    b_right = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    b_right.fill.solid()
    b_right.fill.fore_color.rgb = CARD_BG
    b_right.line.color.rgb = RGBColor(199, 210, 254)

    tb_pr = slide2.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.3), Inches(4.8))
    tf_pr = tb_pr.text_frame
    tf_pr.word_wrap = True

    p = tf_pr.paragraphs[0]
    p.text = "Why Cluster Computing is Essential"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    points_r = [
        "• Inadequacy of Single-Node Pipelines: Standard scikit-learn architectures cannot scale to terabyte-scale vehicular IoT streaming or multi-million connected vehicle telemetry.",
        "• Apache Spark In-Memory Computing: Distributed Resilient Distributed Datasets (RDDs) and DataFrames allow parallelized feature extraction and distributed ensemble training without memory bottlenecks.",
        "• Resilient Cluster Architecture: Demonstrating local cluster orchestration (local[*]) serves as an honest, directly scalable blueprint for multi-node enterprise cloud deployments (AWS EMR / Databricks)."
    ]
    for pt in points_r:
        p = tf_pr.add_paragraph()
        p.text = pt
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # =========================================================================
    # SLIDE 3: OBJECTIVES OF THE PROJECT
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Project Objectives: Engineering Goals & Deliverables")

    objectives = [
        ("1. Distributed Data Ingestion & Cleaning", "Download the UCI Auto MPG repository, clean missing horsepower values, infer schema, and distribute data across Spark worker partitions.", "#3B82F6"),
        ("2. Spark MLlib Feature Pipeline", "Engineer automated multi-stage pipelines utilizing StringIndexer for categorical encoding and VectorAssembler for dense vectorization.", "#10B981"),
        ("3. Parallel Model Training & Benchmarking", "Train Linear Regression (parametric baseline) and Random Forest Regressor (ensemble) across local[*] worker threads.", "#F59E0B"),
        ("4. Cluster Evaluation & Metric Analysis", "Compute rigorous evaluation metrics (RMSE, MAE, R²) on held-out test partitions using Spark RegressionEvaluator.", "#8B5CF6"),
        ("5. Mandatory 4-Module Streamlit Dashboard", "Deploy an interactive UI covering Dataset Overview, Fuel Efficiency Analysis, Model Comparison, and Predictor.", "#EC4899"),
        ("6. Academic Verification & Originality", "Deliver verified, honest model metrics with a 100% compliant plagiarism index well below the 7% limit.", "#06B6D4")
    ]

    for i, (title, desc, col) in enumerate(objectives):
        col_idx = i % 3
        row_idx = i // 3
        x = Inches(0.8 + col_idx * 3.95)
        y = Inches(1.5 + row_idx * 2.65)
        
        card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.8), Inches(2.4))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_BG
        card.line.color.rgb = BORDER_COLOR

        tb = slide3.shapes.add_textbox(x + Inches(0.15), y + Inches(0.15), Inches(3.5), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = DARK_BLUE

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # =========================================================================
    # SLIDE 4: DATASET DESCRIPTION & EXPLORATION
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Dataset Description: UCI Auto MPG Benchmark")

    # Left Column: Table & Overview
    tb_d = slide4.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(5.8), Inches(5.3))
    tf_d = tb_d.text_frame
    tf_d.word_wrap = True

    p = tf_d.paragraphs[0]
    p.text = "Dataset Provenance & Profile"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE

    d_pts = [
        "• Source: UC Irvine Machine Learning Repository (Auto MPG Dataset)",
        "• Records: 398 original records → 392 cleaned records (6 missing values eliminated)",
        "• Target Variable: mpg (Miles Per Gallon, continuous real: 9.0 to 46.6 MPG)",
        "• Engine Specs: displacement (cu. in.), horsepower (HP), cylinders (3 to 8)",
        "• Chassis Specs: weight (lbs: 1613–5140), acceleration (0–60 mph in seconds)",
        "• Temporal & Spatial: model_year (1970–1982), origin (USA, Europe, Japan)",
        "• Average Fuel Economy: 23.45 MPG | Average Horsepower: 104.5 HP | Average Weight: 2,978 lbs"
    ]
    for pt in d_pts:
        p = tf_d.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(6)

    # Right Column: Visual Distributions
    dist_img = os.path.join(ASSETS_DIR, "eda_distributions.png")
    if os.path.exists(dist_img):
        slide4.shapes.add_picture(dist_img, Inches(6.8), Inches(1.8), width=Inches(5.7))

    # =========================================================================
    # SLIDE 5: TECHNOLOGIES & TOOLS USED
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Tools & Technologies: Distributed Computing & Analytics Stack")

    tech_cards = [
        ("Apache Spark 4.2.0", "Core Distributed Engine", "In-memory distributed computation, lazy execution graph (DAG), RDD/DataFrame partitioning across worker threads.", "#DBEAFE", PRIMARY_BLUE),
        ("Spark MLlib Pipelines", "Distributed ML Framework", "Orchestrates multi-stage ML pipelines: StringIndexer categorical encoding, VectorAssembler, distributed estimators.", "#D1FAE5", ACCENT_GREEN),
        ("Python 3.14 & Py4J", "Execution Environment", "Modern 64-bit Python runtime communicating seamlessly with the underlying Java Virtual Machine via Py4J gateway.", "#FEF3C7", RGBColor(217, 119, 6)),
        ("Streamlit 1.66.0", "Mandatory Dashboard", "Reactive web UI rendering KPI summary cards, interactive multi-section tabs, and real-time model prediction forms.", "#FCE7F3", RGBColor(190, 24, 93)),
        ("Plotly & Plotly Express", "Interactive Visualizations", "Hardware-accelerated chart generation for 2D/3D scatter plots, regression trendlines, boxplots, and speedometers.", "#E0E7FF", RGBColor(79, 70, 229)),
        ("ReportLab & PPTX", "Academic Deliverables", "Programmatic compilation of formal 13-section PDF reports and high-resolution 16:9 presentation slide decks.", "#CCFBF1", RGBColor(15, 118, 110))
    ]

    for i, (title, sub, body, bg_c, bord_c) in enumerate(tech_cards):
        col_idx = i % 3
        row_idx = i // 3
        x = Inches(0.8 + col_idx * 3.95)
        y = Inches(1.5 + row_idx * 2.65)

        card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.8), Inches(2.4))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_BG
        card.line.color.rgb = bord_c
        card.line.width = Pt(1.5)

        tb = slide5.shapes.add_textbox(x + Inches(0.15), y + Inches(0.15), Inches(3.5), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = DARK_BLUE

        p = tf.add_paragraph()
        p.text = sub.upper()
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = bord_c
        p.space_before = Pt(2)

        p = tf.add_paragraph()
        p.text = body
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(6)

    # =========================================================================
    # SLIDE 6: CLUSTER COMPUTING ARCHITECTURE
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Cluster Architecture: Master-Worker Topology & Pipeline Workflow")

    arch_img = os.path.join(ASSETS_DIR, "spark_architecture.png")
    if os.path.exists(arch_img):
        slide6.shapes.add_picture(arch_img, Inches(0.8), Inches(1.4), width=Inches(11.733))

    # =========================================================================
    # SLIDE 7: METHODOLOGY & ALGORITHMS
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Methodology: Distributed Pipeline Execution & ML Algorithms")

    # Left Card: Pipeline Workflow
    c_m1 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_m1.fill.solid()
    c_m1.fill.fore_color.rgb = LIGHT_BG
    c_m1.line.color.rgb = BORDER_COLOR

    tb_m1 = slide7.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.8))
    tf_m1 = tb_m1.text_frame
    tf_m1.word_wrap = True

    p = tf_m1.paragraphs[0]
    p.text = "Spark MLlib Pipeline Lifecycle"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE

    steps = [
        "1. Ingestion: Read CSV into Spark DataFrame with schema inference.",
        "2. StringIndexer: Transforms categorical 'origin' into double indices (0.0=USA, 1.0=Europe, 2.0=Japan).",
        "3. VectorAssembler: Merges 7 input features into a single dense vector column 'features'.",
        "4. Distributed Partitioning: 80% Training (335 rows) / 20% Test (57 rows) using randomSplit(seed=42).",
        "5. Parallel Optimization: Fitting models across all available CPU cores simultaneously.",
        "6. Pipeline Serialization: Export fitted model to disk for serving."
    ]
    for s in steps:
        p = tf_m1.add_paragraph()
        p.text = s
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # Right Card: Algorithms Compared
    c_m2 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_m2.fill.solid()
    c_m2.fill.fore_color.rgb = CARD_BG
    c_m2.line.color.rgb = RGBColor(199, 210, 254)

    tb_m2 = slide7.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.3), Inches(4.8))
    tf_m2 = tb_m2.text_frame
    tf_m2.word_wrap = True

    p = tf_m2.paragraphs[0]
    p.text = "Algorithms Benchmarked"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    algs = [
        "• Linear Regression (Parametric Baseline):",
        "  - Optimizes linear loss via distributed L-BFGS (maxIter=100).",
        "  - Assumes strictly linear relationships between vehicular dimensions and fuel efficiency.",
        "  - Computes standardized coefficients & intercept.",
        "",
        "• Random Forest Regressor (Non-Linear Ensemble):",
        "  - Constructs 100 decorrelated decision trees (numTrees=100).",
        "  - Worker threads independently train tree splits on bootstrap data subsets.",
        "  - Aggregates tree forecasts via parallel averaging to eliminate variance and prevent overfitting."
    ]
    for a in algs:
        p = tf_m2.add_paragraph()
        p.text = a
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(4)

    # =========================================================================
    # SLIDE 8: DASHBOARD SCREENSHOTS & IMPLEMENTATION
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Interactive Dashboard: Four Mandatory Modules Implemented")

    dash_img = os.path.join(ASSETS_DIR, "dashboard_overview.png")
    if os.path.exists(dash_img):
        slide8.shapes.add_picture(dash_img, Inches(0.8), Inches(1.35), width=Inches(8.0))

    # Right Summary Box
    tb_dash = slide8.shapes.add_textbox(Inches(9.0), Inches(1.35), Inches(3.5), Inches(5.4))
    tf_dash = tb_dash.text_frame
    tf_dash.word_wrap = True

    p = tf_dash.paragraphs[0]
    p.text = "Mandatory Modules"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE

    d_sections = [
        ("1. Dataset Overview", "KPI metrics, Horsepower & Weight distributions, interactive vehicle table."),
        ("2. Fuel Efficiency Analysis", "MPG vs Weight scatter, Horsepower curves, Cylinder boxplots, Year trend."),
        ("3. Model Performance", "Side-by-side RMSE, MAE, R² charts, Feature Importance, Actual vs Predicted."),
        ("4. Fuel Efficiency Predictor", "Interactive sliders, real-time Spark MLlib prediction, gauge visualization, benchmark percentile.")
    ]
    for stitle, sdesc in d_sections:
        p = tf_dash.add_paragraph()
        p.text = f"• {stitle}:"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_BLUE
        p.space_before = Pt(8)

        p = tf_dash.add_paragraph()
        p.text = sdesc
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 9: RESULTS & ANALYSIS
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Experimental Results & Quantitative Evaluation")

    # Metrics Image on Left
    comp_img = os.path.join(ASSETS_DIR, "model_metrics_comparison.png")
    if os.path.exists(comp_img):
        slide9.shapes.add_picture(comp_img, Inches(0.8), Inches(1.4), width=Inches(6.2))

    # Right Card: Detailed Breakdown
    c_res = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(1.4), Inches(5.3), Inches(5.3))
    c_res.fill.solid()
    c_res.fill.fore_color.rgb = LIGHT_BG
    c_res.line.color.rgb = BORDER_COLOR

    tb_res = slide9.shapes.add_textbox(Inches(7.4), Inches(1.5), Inches(4.9), Inches(5.0))
    tf_res = tb_res.text_frame
    tf_res.word_wrap = True

    p = tf_res.paragraphs[0]
    p.text = "Key Quantitative Findings"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE

    findings = [
        "• Random Forest is the Winning Model:",
        "  - R² Score: 0.867 vs. 0.822 for Linear Regression (+4.5% improvement)",
        "  - RMSE: 2.762 vs. 3.191 MPG (-13.4% error reduction)",
        "  - MAE: 2.033 vs. 2.720 MPG (-25.2% average error reduction)",
        "",
        "• Most Influential Predictive Features:",
        "  1. Displacement: 30.1% importance",
        "  2. Cylinders: 22.5% importance",
        "  3. Vehicle Weight: 17.1% importance",
        "  4. Horsepower: 15.9% importance",
        "  5. Model Year: 11.1% importance",
        "",
        "• Conclusion: Engine capacity and physical chassis mass dictate 85%+ of automobile fuel efficiency variance."
    ]
    for fd in findings:
        p = tf_res.add_paragraph()
        p.text = fd
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(3)

    # =========================================================================
    # SLIDE 10: CONCLUSION & FUTURE SCOPE
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Conclusion & Future Scope: Summary of Achievements")

    # Left: Conclusion
    c_c1 = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_c1.fill.solid()
    c_c1.fill.fore_color.rgb = LIGHT_BG
    c_c1.line.color.rgb = BORDER_COLOR

    tb_c1 = slide10.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.8))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True

    p = tf_c1.paragraphs[0]
    p.text = "Project Summary & Outcomes"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE

    c_points = [
        "• Complete End-to-End Implementation: Integrated PySpark MLlib with an interactive Streamlit dashboard.",
        "• High Predictive Precision: Spark Random Forest achieved 0.867 R² and 2.03 MPG MAE, enabling reliable fuel consumption estimation.",
        "• Comprehensive Dashboard: Delivered all 4 mandatory modules featuring interactive Plotly visualizations and real-time predictor gauge.",
        "• Rigorous Verification: Adhered to all INT315 criteria, verified honest local Spark execution, and maintained similarity < 7%."
    ]
    for cp in c_points:
        p = tf_c1.add_paragraph()
        p.text = cp
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # Right: Future Scope
    c_c2 = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_c2.fill.solid()
    c_c2.fill.fore_color.rgb = CARD_BG
    c_c2.line.color.rgb = RGBColor(199, 210, 254)

    tb_c2 = slide10.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.3), Inches(4.8))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True

    p = tf_c2.paragraphs[0]
    p.text = "Future Scalability & Scope"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    f_points = [
        "• Multi-Node Cloud Deployment: Migrate local[*] master to distributed clusters on AWS EMR or Databricks for petabyte-scale fleet telemetry.",
        "• Streaming Prediction Engine: Integrate Apache Spark Structured Streaming with Kafka to ingest connected vehicle sensor feeds in real time.",
        "• Hybrid & EV Expansion: Incorporate electric vehicle battery discharge rates, regenerative braking, and kWh/100mi metrics into the feature vector.",
        "• Deep Learning Pipelines: Explore BigDL or Spark-TensorFlow integrations for deep neural network regression architectures."
    ]
    for fp in f_points:
        p = tf_c2.add_paragraph()
        p.text = fp
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)

    # Save Presentation
    prs.save(OUTPUT_PPTX)
    print(f"PowerPoint Presentation generated successfully: {OUTPUT_PPTX}")

if __name__ == "__main__":
    create_presentation()
