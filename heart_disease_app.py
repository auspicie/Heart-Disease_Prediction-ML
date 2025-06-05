import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open('heart_disease_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Set up Streamlit UI
st.set_page_config(page_title="Heart Disease Prediction App")
st.title("🫀 Heart Disease Prediction App")

st.write("Enter the following information to predict the risk of heart disease:")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120)
sex = st.selectbox("Sex", ["Male(1)", "Female(0)"])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)")
chol = st.number_input("Cholesterol Level (chol)")
fbs = st.selectbox("Fasting Blood Sugar (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)")
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)")
slope = st.selectbox("Slope of the ST Segment (slope)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Convert categorical input
sex = 1 if sex == "Male" else 0

# Feature vector
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                        exang, oldpeak, slope, ca, thal]])

# Scale input
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    if prediction == 1:
        st.error("⚠️ Likely to have heart disease.")
    else:
        st.success("✅ Unlikely to have heart disease.")
