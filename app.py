import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Diabetes Prediction", layout="centered")
st.title("🩺 Diabetes Prediction App")

# Load model safely
try:
    model = joblib.load("diabetes_pipeline.joblib")
    st.success("Model loaded successfully")
except Exception as e:
    st.error(f"Model loading error: {e}")
    st.stop()

st.write("Enter patient details:")

# Layout
col1, col2 = st.columns(2)

with col1:
    preg = st.number_input("Pregnancies", 0, 20)
    glucose = st.number_input("Glucose", 0, 200)
    bp = st.number_input("Blood Pressure", 0, 200)
    skin = st.number_input("Skin Thickness", 0, 100)
with col2:
    insulin = st.number_input("Insulin", 0, 900)
    bmi = st.number_input("BMI", 0.0, 70.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
    age = st.number_input("Age", 1, 120)

if st.button("Predict"):
    input_df = pd.DataFrame([[preg, glucose, bp, skin, insulin, bmi, dpf, age]],
        columns=["Pregnancies","Glucose","BloodPressure",
                 "SkinThickness","Insulin","BMI",
                 "DiabetesPedigreeFunction","Age"])

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0]

    st.subheader("🧾 Result")

    if prediction == 1:
        st.error(f"⚠️ Diabetic ({prob[1]*100:.2f}%)")
    else:
        st.success(f"✅ Not Diabetic ({prob[0]*100:.2f}%)")

   