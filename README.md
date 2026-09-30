# Insurance Prediction

## Project Overview
This project predicts medical insurance charges based on personal and health-related information.

## Features
- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region

## Machine Learning
- Data preprocessing
- Missing value handling
- Feature scaling
- One-hot encoding
- Outlier transformation
- Linear Regression

## Model Evaluation
- MAE
- RMSE
- R² Score

## Project Structure

Insurance Prediction/
│
├── insurance.ipynb
├── insurance_model.pkl
├── frontend/
│   └── main.py
└── README.md

## How to Run

Install the required libraries:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run frontend/main.py

## Output

The application takes user information and predicts the estimated insurance charges.
