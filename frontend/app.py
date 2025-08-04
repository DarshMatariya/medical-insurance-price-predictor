import streamlit as st
import requests

st.set_page_config(page_title="Insurance Predictor", page_icon="💰")
st.title("Medical Insurance Price Predictor")

# Input
age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI - Body Mass Index", min_value=10.0, max_value=50.0, value=30.0, step=1.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
smoker = st.selectbox("Smoker?", ["Yes", "No"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict Insurance Cost"):
    input_data = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }

    try:
        res = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        prediction = res.json()["predicted_insurance_charge"]
        st.success(f"💰 Estimated Insurance Cost: ₹{prediction}")
    except:
        st.error("API request failed. Is the FastAPI backend running?")
