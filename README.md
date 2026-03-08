# Retail Store Cannibalization Risk Predictor

This project predicts the risk of **store cannibalization**, where nearby stores comepete for the same customers, potentially reducing sales.

The model analyzes store performance metrics such as:
- Average Sales
- Average Customers
- Promotion Frequency
- Distance to Competitor
- Sales Volatality
- Customer Drop Percentage

Based on these features, the model estimates the **probability that a store is at the risk of cannibalization**.

---

## Machine Learning Model
Gradient Boosting Classifier

---

## Features Used
- Avg_Sales – Average daily sales of the store
- Avg_Customers – Average number of customers per day
- PromoFrequency – Fraction of time promotions are active
- HasPromo2 – Indicates long-term promotional participation
- CompetitionDistance – Distance to nearest competitor
- Sales_Std – Sales volatility
- CustomerDropPer – Percentage drop in customers

---

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy

---

## How to Run the App Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the streamlit app:
```bash
streamlit run app.py
```
