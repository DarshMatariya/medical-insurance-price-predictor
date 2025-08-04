from fastapi import FastAPI
from pydantic import BaseModel
from model_logic import predict_insurance
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS so Streamlit can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


class InsuranceInput(BaseModel):
    age: float
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

@app.post("/predict")
def predict(data: InsuranceInput):
    prediction = predict_insurance(data.model_dump())
    return {"predicted_insurance_charge": prediction}
