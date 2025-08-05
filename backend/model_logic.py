import joblib
import numpy as np
import os

# Try to load model from different possible locations
model = None
model_paths = [
    "insurance_rf_model.pkl",
    "./insurance_rf_model.pkl",
    os.path.join(os.path.dirname(__file__), "insurance_rf_model.pkl")
]

for path in model_paths:
    if os.path.exists(path):
        try:
            model = joblib.load(path)
            print(f"Model loaded successfully from: {path}")
            break
        except Exception as e:
            print(f"Failed to load model from {path}: {e}")
            continue

if model is None:
    print("ERROR: Model file 'insurance_rf_model.pkl' not found!")
    raise FileNotFoundError("Model file not found. Please ensure 'insurance_rf_model.pkl' is in the project directory.")

def predict_insurance(data):
    if model is None:
        raise Exception("Model not loaded")
    
    age = data['age']
    sex = 1 if data['sex'].lower() == 'male' else 0
    bmi = data['bmi']
    children = data['children']
    smoker = 1 if data['smoker'].lower() == 'yes' else 0
    region = data['region'].lower()

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