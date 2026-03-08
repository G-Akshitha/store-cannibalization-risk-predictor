import streamlit as st
import pickle
import pandas as pd

# Page settings
st.set_page_config(page_title="Store Cannibalization Risk Predictor", layout="wide")

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


st.title("Retail Store Cannibalization Risk Predictor")

st.markdown("""
This application predicts whether a store is at risk of **cannibalization** 
from nearby competing stores based on sales trends and customer behavior.
""")

# Sidebar
st.sidebar.header("About")
st.sidebar.write("""
Machine Learning Model: Gradient Boosting

This tool predicts cannibalization risk using store sales,
customer trends, and competition distance.
""")

# Layout
col1, col2 = st.columns(2)

# -------------------------
# Column 1
# -------------------------
with col1:

    st.subheader("Sales & Customer Metrics")

    Avg_Sales = st.number_input(
        "Average Sales",
        min_value=0.0,
        max_value=30000.0,
        value=6000.0,
        step=100.0,
        help="Average sales per day for the store"
    )

    Avg_Customers = st.number_input(
        "Average Customers",
        min_value=0.0,
        max_value=3500.0,
        value=600.0,
        step=10.0,
        help="Average number of customers per day"
    )

    Sales_Std = st.number_input(
        "Sales Volatility (Std Dev)",
        min_value=0.0,
        max_value=2000.0,
        value=600.0,
        step=10.0,
        help="Variation in sales levels"
    )

    CustomerDropPer = st.number_input(
        "Customer Drop Percentage",
        min_value=-50.0,
        max_value=100.0,
        value=0.0,
        step=1.0,
        help="Percentage drop in customers after competitor entry"
    )

# -------------------------
# Column 2
# -------------------------
with col2:

    st.subheader("Competition & Promotion")

    CompetitionDistance = st.number_input(
        "Distance to Nearest Competitor (meters)",
        min_value=0.0,
        max_value=30000.0,
        value=1000.0,
        step=100.0,
        help="Distance to the nearest competing store"
    )

    PromoFrequency = st.slider(
        "Promotion Frequency",
        0.0,
        1.0,
        value=0.3,
        help="Fraction of time promotions run"
    )

    promo2_option = st.selectbox(
        "Long-Term Promotion (Promo2)",
        ["No", "Yes"]
    )

    HasPromo2 = 1 if promo2_option == "Yes" else 0

# -------------------------
# Prediction
# -------------------------
if st.button("Predict Cannibalization Risk"):

    try:

        # Arrange features in same order as training
        features = pd.DataFrame({
            "Avg_Sales" : [Avg_Sales],
            "Avg_Customers" : [Avg_Customers],
            "PromoFrequency": [PromoFrequency],
            "HasPromo2": [HasPromo2],
            "CompetitionDistance": [CompetitionDistance],
            "Sales_Std": [Sales_Std],
            "CustomerDropPer": [CustomerDropPer]
        })

        # Predict
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        risk_score = probability * 100

        st.subheader("Prediction Result")

        st.metric("Cannibalization Risk Score", f"{risk_score:.2f}%")

        if risk_score > 70:
            st.error("High Cannibalization Risk")

        elif risk_score > 30:
            st.warning("Medium Cannibalization Risk")

        else:
            st.success("Low Cannibalization Risk")

    except Exception as e:
        st.error("Error making prediction. Please check inputs.")
        st.write(e)