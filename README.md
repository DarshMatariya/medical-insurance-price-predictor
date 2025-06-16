# Medical Insurance Price Predictor

Predict a person’s annual medical insurance charges using demographic and lifestyle features through a supervised machine learning model.

---

## Project Overview

This project focuses on predicting the medical insurance cost for individuals based on attributes like age, BMI, smoking habits, and region. The dataset is sourced from Kaggle, and a Random Forest Regressor was used to model the relationships between features and cost.

---

## Repository Structure

- `notebook/`: Contains the complete Jupyter notebook with data preprocessing, model training, evaluation, and visualizations.
- `dataset/`: Includes a text file with dataset source and feature details. Dataset not uploaded due to size.
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

2. Navigate to the notebook folder:  
   cd notebook  

3. Open and run the Colab notebook named 'medical_insurance_price_prediction.ipynb'.


Feel free to open issues or submit pull requests for improvements.  
