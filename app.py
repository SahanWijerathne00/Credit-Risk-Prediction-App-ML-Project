import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("best_xgb_credit_model.pkl")
encoders = {col: joblib.load(f"{col}_encoder.pkl") for col in ["Sex", "Housing", "Saving accounts", "Checking account"]}

# Page configuration
st.set_page_config(page_title="Credit Risk Predictor", page_icon="💳", layout="centered")

# Dark mode styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #f5f5f5;
        }
        .title {
            text-align: center;
            color: #00e0ff;
            font-size: 40px;
            font-weight: 800;
            text-shadow: 0 0 10px #00e0ff;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #cccccc;
            margin-bottom: 40px;
        }
        label, .stSelectbox label, .stNumberInput label {
            font-weight: 600 !important;
            color: #dcdcdc !important;
        }
        .stTextInput, .stNumberInput, .stSelectbox {
            color: #111 !important;
        }
        .stButton>button {
            background: linear-gradient(90deg, #00e0ff, #0072ff);
            color: white;
            border-radius: 12px;
            padding: 0.8rem 2.5rem;
            font-size: 18px;
            font-weight: 700;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(0, 224, 255, 0.5);
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 25px rgba(0, 224, 255, 0.8);
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title">💳 Credit Risk Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict whether an applicant has a <b>Good</b> or <b>Bad</b> credit risk.</div>', unsafe_allow_html=True)

# Input fields
age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex", options=["male", "female"])
job = st.number_input("Job (0 - 3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", ["own", "rent", "free"])
saving_accounts = st.selectbox("Saving Accounts", ["little", "moderate", "rich", "quite rich"])
checking_account = st.selectbox("Checking Account", ["little", "moderate", "rich"])
credit_amount = st.number_input("Credit Amount", min_value=0, value=1000)
duration = st.number_input("Duration (in months)", min_value=1, value=12)

# Prepare input data
input_df = pd.DataFrame({
    "Age": [age],
    "Sex": [encoders["Sex"].transform([sex])[0]],
    "Job": [job],
    "Housing": [encoders["Housing"].transform([housing])[0]],
    "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
    "Checking account": [encoders["Checking account"].transform([checking_account])[0]],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

# Predict button
if st.button("🔍 Predict Risk"):
    prediction = model.predict(input_df)
    
    if prediction == 1:
        st.balloons()
        st.toast("💰 The applicant has a **GOOD Credit Risk!**", icon="✅")
    else:
        st.snow()
        st.toast("💣 The applicant has a **BAD Credit Risk!**", icon="⚡")
