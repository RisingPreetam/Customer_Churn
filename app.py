import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("churn_model.pkl")
columns = joblib.load("columns.pkl")

st.title("Customer Churn Prediction")

# Inputs
tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges")

gender = st.selectbox("Gender", ["Male", "Female"])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])

# ===== ENCODING =====
gender = 1 if gender == "Male" else 0
Partner = 1 if Partner == "Yes" else 0
Dependents = 1 if Dependents == "Yes" else 0

input_dict = {
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "gender": gender,
    "Partner": Partner,
    "Dependents": Dependents,
}

input_df = pd.DataFrame([input_dict])

# Ensure same column order
input_df = input_df.reindex(columns=columns, fill_value=0)

# Prediction button
if st.button("Predict"):
    
    # ⚠️ IMPORTANT: features order same hona chahiye jo training me tha
    input_data = np.array([[tenure, monthly_charges]])
    
    result = model.predict(input_data)
    
    if result[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")