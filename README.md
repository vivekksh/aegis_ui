# AegisAI ⚡  
**Intelligent Energy Forecasting with Uncertainty Awareness**

AegisAI is an end-to-end AI/ML project that predicts short-term energy consumption using machine learning, uncertainty estimation, and a modern full-stack architecture.

The system is designed to demonstrate real-world ML engineering skills, including data processing, model training, inference APIs, explainability, and a production-ready frontend.

---

## 🔍 Project Overview

AegisAI forecasts energy usage based on:
- Time context (hour, day of week, month)
- Recent energy consumption patterns
- Rolling statistics for trend awareness

The system provides:
- **Point forecasts**
- **Confidence intervals (uncertainty estimation)**
- **Explainability support (SHAP-ready)**
- **A clean, interactive UI**

---

## 🧠 Key Features

- 🔮 **Machine Learning Forecasting**
  - Trained regression model for short-term energy prediction
- 📊 **Uncertainty Estimation**
  - Prediction intervals to indicate forecast reliability
- 🧩 **Feature Engineering**
  - Lag features and rolling averages
- 🧠 **Explainability**
  - SHAP-based model interpretability (offline)
- 🌐 **FastAPI Backend**
  - RESTful inference APIs
- 🎨 **React Frontend**
  - Clean UI with Dark / Light mode
- 🛡️ **Robust UI Design**
  - Graceful handling of unavailable forecasts
  - Safe rendering (no crashes)

---


---

## ⚙️ Backend Details

- **Framework**: FastAPI
- **ML Stack**:  
  - NumPy, Pandas  
  - Scikit-learn  
  - SHAP (explainability)
- **Model Type**: Regression-based energy forecasting model
- **Endpoints**:
  - `/predict/multi-horizon` – multi-horizon energy forecast

> ⚠️ Trained model files are not committed to GitHub to keep the repository lightweight.

---

## 🎨 Frontend Details

- **Framework**: React (Create React App)
- **Styling**: Tailwind CSS
- **Features**:
  - User-friendly input form
  - Forecast cards with confidence ranges
  - Dark / Light theme toggle
  - Clear system status indicators

---

## 🚀 Running Locally

### 1️⃣ Backend

```bash
cd sentinelml
pip install -r requirements.txt
uvicorn backend.app:app --reload



---

# ✅ WHAT YOU DO NOW (VERY SIMPLE)

1️⃣ In your repo root (`aegis-ai/`), create **`README.md`**  
2️⃣ Paste **the entire content above**  
3️⃣ Save the file  
4️⃣ Commit & push:

```bash
git add README.md
git commit -m "Add project README"
git push
