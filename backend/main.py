import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model_logic import predict_insurance
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Insurance Predictor API", version="1.0.0")

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

@app.get("/")
def root():
    return {"message": "Insurance Predictor API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: InsuranceInput):
    try:
        prediction = predict_insurance(data.model_dump())
        return {"predicted_insurance_charge": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)