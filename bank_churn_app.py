#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import necessary libraries
import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the saved model
with open('bank_churn.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the web app
st.title("Bank Churn Prediction App")

# User input function with one-hot encoding for Geography and Gender
def get_user_input():
    credit_score = st.number_input("Credit Score", min_value=0, step=1)
    geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    tenure = st.number_input("Tenure", min_value=0, max_value=10, step=1)
    balance = st.number_input("Balance", min_value=0.0, format="%.2f")
    num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, step=1)
    has_cr_card = st.selectbox("Has Credit Card", [1, 0])
    is_active_member = st.selectbox("Is Active Member", [1, 0])
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, format="%.2f")

    # One-hot encoding for Geography
    geography_france = 1 if geography == "France" else 0
    geography_spain = 1 if geography == "Spain" else 0
    geography_germany = 1 if geography == "Germany" else 0

    # Encoding Gender as binary
    gender_male = 1 if gender == "Male" else 0
    gender_female = 1 if gender == "Female" else 0

    # Encoding other fields as binary
    has_cr_card = 1 if has_cr_card == "Yes" else 0
    is_active_member = 1 if is_active_member == "Yes" else 0

    # Creating a DataFrame for the model input
    data = {
        'CreditScore': credit_score,
        'Geography_France': geography_france,
        'Geography_Spain': geography_spain,
        'Geography_Germany': geography_germany,
        'Gender_Male': gender_male,
        'Gender_Female': gender_female,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_of_products,
        'HasCrCard': has_cr_card,
        'IsActiveMember': is_active_member,
        'EstimatedSalary': estimated_salary
    }

    features = pd.DataFrame(data, index=[0])
    return features

# Display input fields and collect user input
user_input = get_user_input()

# Display user input if needed
st.subheader("User Input Features")
st.write(user_input)

# Prediction
if st.button("Predict"):
    prediction = model.predict(user_input)
    churn_status = "Exited" if prediction[0] == 1 else "Stayed"
    st.subheader("Prediction")
    st.write(f"The customer is likely to **{churn_status}**.")


# In[ ]:




