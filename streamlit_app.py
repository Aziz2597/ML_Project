import streamlit as st
import requests
import json

# Set FastAPI backend URL (update this if deployed online)
FASTAPI_URL = "http://127.0.0.1:5000/predict"

# Streamlit UI
st.title("🏡 House Price Prediction App")
st.write("Enter the house details below to get a price estimate.")

# Input fields
num_features = st.number_input("Number of Features", min_value=1, max_value=20, value=7, help="Enter the number of numerical features")

features = []
for i in range(num_features):
    feature = st.number_input(f"Feature {i+1}", value=0.0, format="%.2f")
    features.append(feature)

# Button to make prediction
if st.button("Predict Price"):
    try:
        # Send request to FastAPI
        response = requests.post(FASTAPI_URL, json={"features": features})

        # Process response
        if response.status_code == 200:
            result = response.json()
            st.success(f"🏠 Predicted House Price: ₹{result['predicted_price']:.2f}")
        else:
            st.error(f"❌ Error: {response.json()['detail']}")
    
    except requests.exceptions.RequestException as e:
        st.error(f"🚨 Connection Error: {str(e)}")
