# 🏡 House Price Prediction - ML Project

This project provides an **ML-powered API** and **frontend UI** for predicting house prices based on input features.

---

## 📌 Features
✅ **FastAPI-based REST API** for predictions  
✅ **Streamlit UI** for user-friendly interaction  
✅ **Trained Random Forest Model** for house price estimation  
✅ **Docker-ready** and deployable on cloud platforms  

---

## 📂 Project Structure
```
ML_project/
│── fastapi_app.py
│── best_random_forest_model.pkl 
├── requirements.txt 
│── streamlit_app.py  
│── SoulAI_ML.ipynb   
│── .gitignore
│── README.md  
```

---

## 🚀 Setup and Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/ML_project.git
cd ML_project
```

### 2️⃣ Create and Activate Virtual Environment (Recommended)
```sh
python -m venv venv
# Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 🔧 Running the FastAPI Server

1. Start the FastAPI server:
   ```sh
   uvicorn fastapi_app:app --host 0.0.0.0 --port 5000 --reload
   ```
2. Access the **interactive API docs**:
   - Open **Swagger UI**: [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)  
   - Open **Redoc UI**: [http://127.0.0.1:5000/redoc](http://127.0.0.1:5000/redoc)  

---

## 💡 Making Predictions via API

Use **cURL** or Postman to send a `POST` request:
```sh
curl -X 'POST' 'http://127.0.0.1:5000/predict' \
     -H 'Content-Type: application/json' \
     -d '{"features": [3, 2, 1500, 5000, 2, 0, 1, 3, 7, 1400, 100, 2005, 2010, 47.5, -122.3, 1600, 5200, 3, 15]}'
```
Expected response:
```json
{
    "predicted_price": 450000.0
}
```

---

## 🎨 Running the Streamlit UI

1. Start Streamlit:
   ```sh
   streamlit run streamlit_app.py
   ```
2. Open the browser at **[http://localhost:8501](http://localhost:8501)**  

---

## 🐳 Running with Docker (Optional)

1. Build the Docker image:
   ```sh
   docker build -t house-price-prediction .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 house-price-prediction
   ```

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

