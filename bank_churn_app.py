#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import necessary libraries
import streamlit as st
import pickle
import pandas as pd

# Load the saved model
with open('bank_churn.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the web app
st.title("Bank Churn Prediction App")

# User input function with one-hot encoding for Country and Gender
def get_user_input():
    credit_score = st.number_input("Credit Score", min_value=0, step=1)
    country = st.selectbox("Country", ["France", "Spain", "Germany"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    tenure = st.number_input("Tenure", min_value=0, max_value=10, step=1)
    balance = st.number_input("Balance", min_value=0.0, format="%.2f")
    products_number = st.number_input("Number of Products", min_value=1, max_value=4, step=1)
    credit_card = st.selectbox("Has Credit Card?", [1, 0])
    active_member = st.selectbox("Is Active Member?", [1, 0])
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, format="%.2f")

    # One-hot encoding for Country
    country_France = 1 if country == "France" else 0
    country_Spain = 1 if country == "Spain" else 0
    country_Germany = 1 if country == "Germany" else 0

    # Encoding Gender as binary
    gender_Male = 1 if gender == "Male" else 0
    gender_Female = 1 if gender == "Female" else 0

    # Creating a DataFrame for the model input
    data = {
        'credit_score': credit_score,
        'country_France': country_France,
        'country_Spain': country_Spain,
        'country_Germany': country_Germany,
        'gender_Male': gender_Male,
        'gender_Female': gender_Female,
        'age': age,
        'tenure': tenure,
        'balance': balance,
        'products_number': products_number,
        'credit_card': credit_card,
        'active_member': active_member,
        'estimated_salary': estimated_salary
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




