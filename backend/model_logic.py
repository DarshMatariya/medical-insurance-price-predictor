import joblib
import numpy as np

model = joblib.load("insurance_rf_model.pkl")

def predict_insurance(data):
    age = data['age']
    sex = 1 if data['sex'] == 'male' else 0
    bmi = data['bmi']
    children = data['children']
    smoker = 1 if data['smoker'] == 'yes' else 0
    region = data['region']

    region_encoded = {
        "region_northwest": 0,
        "region_southeast": 0,
        "region_southwest": 0
    }
    if region != "northeast":
        region_encoded[f"region_{region}"] = 1

    # Standardized based on training
    age = (age - 39.2070) / 14.0490
    bmi = (bmi - 30.6634) / 6.0982
    children = (children - 1.0949) / 1.2055

    input_data = [
        age,
        sex,
        bmi,
        children,
        smoker,
        region_encoded["region_northwest"],
        region_encoded["region_southeast"],
        region_encoded["region_southwest"]
    ]

    log_prediction = model.predict([input_data])[0]
    prediction = np.exp(log_prediction)
    return round(prediction, 2)
