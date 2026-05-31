# Product Churn Prediction System

## Overview
This project is an end-to-end Machine Learning and Analytics solution designed to predict whether a product is likely to churn based on historical retail sales behavior. The system analyzes product performance, engineers business-oriented features, trains machine learning models, and deploys the final model using Streamlit for real-time prediction.

---

# Business Problem
In retail and e-commerce businesses, some products gradually stop generating sales, resulting in inventory inefficiencies and revenue loss. Identifying these products early helps businesses take proactive actions such as promotions, pricing optimization, and inventory planning.

This project predicts product churn using historical transaction data and machine learning techniques.

---

# Dataset
Dataset Used:
- Online Retail Dataset (UCI Repository)

The dataset contains:
- Invoice details
- Product descriptions
- Quantity sold
- Unit price
- Invoice dates
- Customer IDs
- Country information

---

# Project Workflow

## 1. Data Cleaning
Performed:
- Missing value handling
- Removed cancelled transactions
- Removed invalid quantities and prices
- Converted date columns
- Duplicate handling

Created:
```python
TotalRevenue = Quantity * UnitPrice
```

---

## 2. Exploratory Data Analysis (EDA)

Performed analysis on:
- Revenue distribution across products
- Product transaction patterns
- Product lifecycle analysis
- Product churn magnitude
- Revenue concentration
- Sales decline before churn
- Product segmentation

### Key Insights
- A small percentage of products generated most of the revenue.
- Products with lower transaction frequency had higher churn probability.
- Revenue efficiency strongly impacted product survival.
- Many products showed declining activity before churning.

---

## 3. Feature Engineering

Created product-level features including:
- Total Revenue
- Total Transactions
- Product Lifetime Days
- Average Revenue per Transaction
- Transaction Frequency
- Revenue Efficiency
- Average Quantity per Transaction

Target Variable:
- `is_churned`
    - 1 = Churned Product
    - 0 = Active Product

---

# Machine Learning Models

Models Implemented:
1. Logistic Regression
2. Random Forest Classifier

---

# Model Evaluation

Evaluation Metrics Used:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

### Final Model Performance (Random Forest)
- Accuracy: ~86%
- Recall: ~85%
- ROC-AUC: ~0.93

Random Forest was selected as the final model because it achieved superior performance in identifying churned products.

---

# Streamlit Deployment

The trained model was deployed using Streamlit.

Features of the application:
- Real-time churn prediction
- Churn probability estimation
- Risk level categorization
- Business recommendations

---

# Technologies Used

## Programming Language
- Python

## Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

# Project Structure

```text
product-churn-prediction/
│
├── data/
│   └── product_level_dataset.csv
│
├── notebooks/
│   ├── 1_data_cleaning.ipynb
│   ├── 2_eda_product_churn.ipynb
│   └── 3_ml_product_churn_prediction.ipynb
│
├── models/
│   ├── best_product_churn_model.pkl
│   └── model_features.pkl
│
├── app.py
├── README.md
└── requirements.txt
```

---

# How to Run the Project

## Clone Repository

```bash
git clone <your-repository-link>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit Application

```bash
streamlit run app.py
```

---

# Future Improvements
Possible future enhancements:
- Time-series forecasting
- Hyperparameter tuning
- Power BI dashboard integration
- Seasonal trend analysis
- Product category analysis
- XGBoost implementation

---

# Business Impact
This system helps businesses:
- Detect at-risk products early
- Reduce revenue loss
- Improve inventory management
- Support proactive decision-making
- Optimize product strategy

---
