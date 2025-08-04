# Medical Insurance Price Prediction 

A full-stack machine learning project to predict medical insurance costs based on user input like age, gender, BMI, number of children, smoking habits and region.  
Built with:
- Python, Scikit-Learn, RandomForestRegressor
- FastAPI (Backend)
- Streamlit (Frontend)
- Deployed on Render / Vercel

---

## Repository Structure

- `notebook/`: Contains the complete Jupyter notebook with data preprocessing, model training, evaluation, and visualizations.
- `dataset/`: Includes a text file with dataset source and feature details. Dataset not uploaded due to size.
- `backend/` : FastAPI backend (model & API)
- `frontend/` : Streamlit frontend (UI)
- `results/`: Holds the prediction plot (actual vs predicted) and model evaluation metrics (MAE, RMSE, R²).

---

## Dataset

- **Source**: [Medical Cost Personal Dataset - Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Features**:
  - Age
  - Sex
  - BMI
  - Number of Children
  - Smoker (Yes/No)
  - Region
  - Charges (Target)

---

## Workflow Overview

- Handle missing/duplicate entries
- Encode categorical variables
- Apply scaling with `StandardScaler`
- Log-transform the `charges` column
- Train `RandomForestRegressor`
- Visualize results and performance metrics

---

## Model

- Algorithm: **Random Forest Regressor**
- Libraries: `pandas`, `scikit-learn`, `numpy`, `matplotlib`
- Metrics:
  - MAE: `2118.36`
  - RMSE: `4411.39`
  - R² Score: `0.8941`

---

## Results

Navigate to the `results/` folder to view:
- 📊 `actual_vs_predicted.png`: scatter plot of predicted vs actual charges
- 📄 `evaluation.txt`: contains MAE, RMSE, and R² values

---


## How to Run This Project

1. Clone the repository:  
   git clone https://github.com/DarshMatariya/medical-insurance-price-predictor.git  

2. Run Backend:
   - cd backend
   - uvicorn main:app --reload

3. Run frontend:
   - cd frontend
   - streamlit run app.py



Feel free to open issues or submit pull requests for improvements.  
