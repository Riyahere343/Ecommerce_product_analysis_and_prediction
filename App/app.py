import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("best_product_churn_model.pkl")
features = joblib.load("model_features.pkl")

st.set_page_config(
    page_title="Product Churn Prediction System",
    layout="centered"
)

st.title("🛒 Product Churn Prediction System")

st.write("""
This app predicts whether a product is likely to churn based on product performance features.
""")

st.subheader("Enter Product Details")

total_revenue = st.number_input("Total Revenue", min_value=0.0, value=500.0)
total_transactions = st.number_input("Total Transactions", min_value=1, value=5)
total_quantity_sold = st.number_input("Total Quantity Sold", min_value=1, value=20)
product_lifetime_days = st.number_input("Product Lifetime Days", min_value=0, value=100)

avg_revenue_per_txn = total_revenue / total_transactions
transaction_frequency = total_transactions / (product_lifetime_days + 1)
revenue_efficiency = total_revenue / (product_lifetime_days + 1)
avg_quantity_per_txn = total_quantity_sold / total_transactions

input_data = pd.DataFrame([{
    "total_revenue": total_revenue,
    "total_transactions": total_transactions,
    "product_lifetime_days": product_lifetime_days,
    "avg_revenue_per_txn": avg_revenue_per_txn,
    "transaction_frequency": transaction_frequency,
    "revenue_efficiency": revenue_efficiency,
    "avg_quantity_per_txn": avg_quantity_per_txn
}])

input_data = input_data[features]

if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    churn_probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Product is likely to churn")
    else:
        st.success("✅ Product is not likely to churn")

    st.write(f"**Churn Probability:** {round(churn_probability * 100, 2)}%")

    if churn_probability < 0.4:
        st.info("Risk Level: Low Risk")
    elif churn_probability < 0.7:
        st.warning("Risk Level: Medium Risk")
    else:
        st.error("Risk Level: High Risk")

    st.subheader("Business Recommendation")

    if churn_probability >= 0.7:
        st.write("Consider discounting, promotion, or reviewing product strategy.")
    elif churn_probability >= 0.4:
        st.write("Monitor product performance and consider targeted marketing.")
    else:
        st.write("Product appears stable. Maintain current strategy.")