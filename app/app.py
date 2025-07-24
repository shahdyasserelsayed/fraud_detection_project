#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd
import joblib

st.title("🛑 Fraud Detection App 🛑 ")
st.write("Welcome to the app! Here you can detect fraud cases.")

# Load model and scaler
model = joblib.load(r"C:\Users\starr\OneDrive\Desktop\fraud_detection_project\model\model.pkl")
scaler = joblib.load(r"C:\Users\starr\OneDrive\Desktop\fraud_detection_project\model\scaler.pkl")

# Upload CSV
uploaded_file = st.file_uploader("Upload transaction CSV", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    # Drop non-feature columns (those not used during training)
    X = data.drop(columns=['Time', 'Class'], errors='ignore')

    # Scale using the same scaler
    X_scaled = scaler.transform(X)

    # Make predictions
    predictions = model.predict(X_scaled)

    # Add prediction column to original data
    data['Prediction'] = predictions
    st.write(data)

    fraud_count = data['Prediction'].sum()
    st.success(f"🚨 {fraud_count} potentially fraudulent transactions detected.")


# In[ ]:




