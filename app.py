# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle

scaler = pickle.load(open("scaler.pkl", "rb"))
pca = pickle.load(open("pca.pkl", "rb"))
model = pickle.load(open("kmeans_model.pkl", "rb"))


# ---------- Streamlit UI ----------
st.set_page_config(page_title="Credit Risk Cluster Predictor", layout="centered")
st.title("💳 Credit Risk Cluster Predictor")
st.markdown("This app assigns customers to one of the credit risk clusters based on their financial and demographic data.")

st.sidebar.header("Enter Customer Information")

# ---------- User Input Form ----------
def user_input():
    age = st.sidebar.slider("Age", 18, 75, 30)
    sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
    job = st.sidebar.slider("Job Type (0=Unskilled , 1=Moderate , 2=Quiet Skilled , 3=Highly Skilled)", 0, 3, 1)
    housing = st.sidebar.selectbox("Housing", ["Own", "Rent", "Free"])
    saving_acct = st.sidebar.selectbox("Saving Account", ["Little", "Moderate", "Quite Rich", "Rich", "Unknown"])
    checking_acct = st.sidebar.selectbox("Checking Account", ["Little", "Moderate", "Rich", "Unknown"])
    credit_amount = st.sidebar.number_input("Credit Amount (€)", 0, 20000, 1000)
    duration = st.sidebar.slider("Duration (months)", 4, 72, 24)
    purpose = st.sidebar.selectbox("Purpose", ["Radio/TV", "Education", "Furniture", "Car", "Business", "Domestic", "Repairs", "Other"])

    # Map values to match LabelEncoded values
    sex_map = {"Male": 1, "Female": 0}
    housing_map = {"Own": 1, "Rent": 2, "Free": 0}
    saving_map = {"Little": 1, "Moderate": 2, "Quite Rich": 3, "Rich": 4, "Unknown": 0}
    checking_map = {"Little": 1, "Moderate": 2, "Rich": 3, "Unknown": 0}
    purpose_map = {"Radio/TV": 5, "Education": 1, "Furniture": 0, "Car": 3, "Business": 2,
                   "Domestic": 4, "Repairs": 6, "Other": 7}

    # Prepare DataFrame
    input_df = pd.DataFrame({
        "Age": [age],
        "Sex": [sex_map[sex]],
        "Job": [job],
        "Housing": [housing_map[housing]],
        "Saving accounts": [saving_map[saving_acct]],
        "Checking account": [checking_map[checking_acct]],
        "Credit amount": [credit_amount],
        "Duration": [duration],
        "Purpose": [purpose_map[purpose]]
    })

    return input_df

# ---------- Run Prediction ----------
user_data = user_input()

scaled_input = scaler.transform(user_data)
pca_input = pca.transform(scaled_input)
cluster = model.predict(pca_input)[0]


# ---------- Output ----------
st.subheader("Predicted Credit Cluster")
st.success(f"The customer falls into **Cluster {cluster}**.")

st.markdown("Clusters are grouped based on financial behavior patterns like credit amount, payment history, account types, etc.")

# Optional: Show raw input
with st.expander("Show Input Data"):
    st.write(user_data)
