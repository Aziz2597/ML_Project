from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import logging

app = FastAPI(title="House Price Prediction API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    model = joblib.load("best_random_forest_model.pkl")
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load model: {str(e)}")
    raise RuntimeError("Model loading failed. Ensure 'best_random_forest_model.pkl' exists.")

logging.basicConfig(
    filename="/content/fastapi_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Define request schema with validation
class HouseFeatures(BaseModel):
    features: list[float] = Field(..., description="List of numerical house features.")

@app.get("/")
def home():
    return {"message": "Welcome to the House Price Prediction API!"}

@app.post("/predict")
def predict(data: HouseFeatures):
    try:
        features = np.array(data.features).reshape(1, -1)  

        expected_features = model.n_features_in_
        if len(data.features) != expected_features:
            raise ValueError(f"Expected {expected_features} features, but got {len(data.features)}.")

        prediction = model.predict(features)[0]
        price = float(prediction)

        logging.info(f"Input: {data.features} | Predicted Price: {price}")

        return {"predicted_price": price}
    
    except ValueError as ve:
        logging.warning(f"Validation Error: {str(ve)}")
        raise HTTPException(status_code=422, detail=str(ve))
    
    except Exception as e:
        logging.error(f"Server Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error. Check logs for details.")
