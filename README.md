# 💳 Credit Risk Prediction App

A machine learning web app that predicts credit risk using XGBoost model with a modern Streamlit interface.

## 🚀 Quick Start

### Installation

```bash
pip install streamlit pandas scikit-learn xgboost joblib
```

### Run the App

```bash
streamlit run app.py
```

## 📊 Features

- Real-time credit risk predictions
- Interactive form with 8 input parameters
- Animated popup results
- Modern glassmorphism UI design

## 📁 Required Files

- `app.py` - Main application
- `best_xgb_credit_model.pkl` - Trained model
- `german_credit_data.csv` - Dataset
- Encoder files: `Sex_encoder.pkl`, `Housing_encoder.pkl`, `Saving accounts_encoder.pkl`, `Checking account_encoder.pkl`

## 💻 Input Parameters

- Age, Sex, Job Level (0-3)
- Housing, Saving Accounts, Checking Account
- Credit Amount, Duration (months)

## 🎯 Output

- ✅ **GOOD** - Low credit risk (approved)
- ⚠️ **BAD** - High credit risk (rejected)

## 🛠️ Tech Stack

Python | Streamlit | XGBoost | Pandas | Scikit-learn
