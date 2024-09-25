import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('health_risk_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Health Risk Calculator")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
sysBP = st.number_input("Systolic Blood Pressure", min_value=80, max_value=200, value=120)
diaBP = st.number_input("Diastolic Blood Pressure", min_value=50, max_value=130, value=80)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
cholesterol = st.number_input("Cholesterol Level", min_value=100, max_value=400, value=180)
diabetes = st.selectbox("Do you have diabetes?", ["No", "Yes"])
smoker = st.selectbox("Are you a smoker?", ["No", "Yes"])

# Prepare input data for prediction
input_data = pd.DataFrame([[age, 1 if gender == "Male" else 0, sysBP, diaBP, bmi, cholesterol, 1 if diabetes == "Yes" else 0, 1 if smoker == "Yes" else 0]],
                          columns=['age', 'gender', 'sysBP', 'diaBP', 'BMI', 'cholesterol', 'diabetes', 'smoker'])

# Make predictions
risk_prediction = model.predict(input_data)[0]
risk_probability = model.predict_proba(input_data)[0][1]

if st.button("Calculate Health Risk"):
    st.write(f"Your predicted risk of heart disease is: {'High' if risk_prediction else 'Low'}")
    st.write(f"Risk probability: {risk_probability:.2f}")
