
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Insurance Prediction",
    page_icon="🏥",
    layout="wide"
)

# Load model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / "insurance_model.pkl"

model = joblib.load(MODEL_PATH)


st.title("🏥 Insurance Charges Prediction")
st.write("Enter patient information to predict insurance charges.")

st.divider()

st.subheader("Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=30
    )

    sex = st.selectbox(
        "Sex",
        ["male", "female"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=70.0,
        value=25.0,
        step=0.1
    )


with col2:
    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=20,
        value=0
    )

    smoker = st.selectbox(
        "Smoker",
        ["yes", "no"]
    )

    region = st.selectbox(
        "Region",
        ["southwest", "southeast", "northwest", "northeast"]
    )


st.divider()


if st.button("🔮 Predict Insurance Charges", use_container_width=True):

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    prediction = model.predict(input_data)

    predicted_charge = prediction[0]

    st.success("Prediction Successful!")

    st.metric(
        "Estimated Insurance Charges",
        f"${predicted_charge:,.2f}"
    )

    st.subheader("Entered Information")

    st.dataframe(
        input_data,
        use_container_width=True
    )