import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

# Inputs
tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges")

# Prediction button
if st.button("Predict"):
    
    # ⚠️ IMPORTANT: features order same hona chahiye jo training me tha
    input_data = np.array([[tenure, monthly_charges]])
    
    result = model.predict(input_data)
    
    if result[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")