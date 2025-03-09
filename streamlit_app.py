import streamlit as st
import requests
import json

FASTAPI_URL = "http://127.0.0.1:5000/predict"

# Feature names
feature_names = [
    "Number of Bedrooms",
    "Number of Bathrooms",
    "Living Area (sq ft)",
    "Lot Area (sq ft)",
    "Number of Floors",
    "Waterfront Present (1 = Yes, 0 = No)",
    "Number of Views",
    "Condition of the House (1-5)",
    "Grade of the House (1-13)",
    "Area of House (Excluding Basement)",
    "Area of the Basement",
    "Built Year",
    "Renovation Year (0 if never renovated)",
    "Latitude",
    "Longitude",
    "Living Area after Renovation",
    "Lot Area after Renovation",
    "Number of Schools Nearby",
    "Distance from Airport (km)",
]

# Streamlit UI
st.title("🏡 House Price Prediction App")
st.write("Enter the house details below to get a price estimate.")

features = []
for i, name in enumerate(feature_names):
    feature = st.number_input(name, value=0.0, format="%.2f")
    features.append(feature)

# Button to make prediction
if st.button("Predict Price"):
    try:
        response = requests.post(FASTAPI_URL, json={"features": features})

        if response.status_code == 200:
            result = response.json()
            st.success(f"🏠 Predicted House Price: ₹{result['predicted_price']:.2f}")
        else:
            st.error(f"❌ Error: {response.json()['detail']}")

    except requests.exceptions.RequestException as e:
        st.error(f"🚨 Connection Error: {str(e)}")
