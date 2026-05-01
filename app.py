import streamlit as st
import joblib
import pandas as pd

# Load pipeline
model = joblib.load("model.pkl")

st.title("🏦 Bank Marketing Prediction")

st.write("Enter customer details:")

# Inputs
age = st.number_input("Age", 18, 100, 30)
balance = st.number_input("Balance", 0, 100000, 1000)
campaign = st.number_input("Campaign", 1, 50, 1)
pdays = st.number_input("Pdays", 0, 999, 0)
previous = st.number_input("Previous", 0, 50, 0)

job = st.selectbox("Job", ["admin.", "blue-collar", "technician", "services"])
marital = st.selectbox("Marital", ["single", "married"])
education = st.selectbox("Education", ["secondary", "tertiary"])
housing = st.selectbox("Housing Loan", ["yes", "no"])
loan = st.selectbox("Personal Loan", ["yes", "no"])
contact = st.selectbox("Contact", ["cellular", "telephone"])

if st.button("Predict"):
    
    # Create base input
    input_dict = {
        'age': age,
        'balance': balance,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
    }
    
    # Create dataframe with ALL columns initialized to 0
    columns = model.named_steps['model'].feature_names_in_
    data = pd.DataFrame(0, index=[0], columns=columns)
    
    # Fill numeric
    for col in input_dict:
        if col in data.columns:
            data[col] = input_dict[col]
    
    # Fill categorical
    data[f'job_{job}'] = 1 if f'job_{job}' in data.columns else 0
    data[f'marital_{marital}'] = 1 if f'marital_{marital}' in data.columns else 0
    data[f'education_{education}'] = 1 if f'education_{education}' in data.columns else 0
    data[f'housing_{housing}'] = 1 if f'housing_{housing}' in data.columns else 0
    data[f'loan_{loan}'] = 1 if f'loan_{loan}' in data.columns else 0
    data[f'contact_{contact}'] = 1 if f'contact_{contact}' in data.columns else 0
    
    # Prediction
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.success("Customer WILL subscribe ✅")
    else:
        st.error("Customer will NOT subscribe ❌")