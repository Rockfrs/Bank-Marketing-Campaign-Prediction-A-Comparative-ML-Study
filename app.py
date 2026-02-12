import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, roc_auc_score, matthews_corrcoef, 
                             confusion_matrix, classification_report)

# Page Setup
st.set_page_config(page_title="Bank Marketing Study", layout="wide")

st.title("🏦 Bank Marketing Campaign Prediction")
st.write("An end-to-end ML study comparing 6 classification models.")

# --- SIDEBAR: Model Selection (Requirement B) ---
st.sidebar.header("Model Configuration")
model_choice = st.sidebar.selectbox(
    "Select a Classification Model", 
    ["Logistic_Regression", "Decision_Tree", "kNN", "Naive_Bayes", "Random_Forest", "XGBoost"]
)

# Load Helper Assets (Scaler and Encoders)
def load_helpers():
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('label_encoders.pkl', 'rb') as f:
        encoders = pickle.load(f)
    return scaler, encoders

# --- MAIN PAGE: Dataset Upload (Requirement A) ---
uploaded_file = st.file_uploader("Upload your test CSV data (Semicolon ';' separated)", type="csv")

if uploaded_file is not None:
    # Read data
    test_df = pd.read_csv(uploaded_file, sep=';')
    st.subheader("Data Preview")
    st.dataframe(test_df.head())

    if st.button(f"Run Analysis with {model_choice}"):
        try:
            scaler, encoders = load_helpers()
            
            # Load selected model
            with open(f'{model_choice}.pkl', 'rb') as f:
                model = pickle.load(f)

            # Preprocessing
            proc_df = test_df.copy()
            for col, le in encoders.items():
                if col in proc_df.columns:
                    proc_df[col] = proc_df[col].map(lambda s: le.transform([s])[0] if s in le.classes_ else -1)

            # Split X and y (assuming 'y' is the target column)
            X_eval = proc_df.drop('y', axis=1)
            y_true = proc_df['y'].map({'no': 0, 'yes': 1})
            
            # Scale and Predict
            X_eval_scaled = scaler.transform(X_eval)
            y_pred = model.predict(X_eval_scaled)
            y_prob = model.predict_proba(X_eval_scaled)[:, 1] if hasattr(model, "predict_proba") else y_pred

            # --- DISPLAY METRICS (Requirement C) ---
            st.subheader(f"📊 Evaluation Metrics: {model_choice}")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Accuracy", f"{accuracy_score(y_true, y_pred):.2%}")
            m2.metric("AUC Score", f"{roc_auc_score(y_true, y_prob):.4f}")
            m3.metric("MCC", f"{matthews_corrcoef(y_true, y_pred):.4f}")
            m4.metric("F1 Score", f"{f1_score(y_true, y_pred):.4f}")

            # --- VISUALS: Confusion Matrix & Report (Requirement D) ---
            st.subheader("📈 Performance Visualization")
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.write("**Confusion Matrix**")
                fig, ax = plt.subplots()
                cm = confusion_matrix(y_true, y_pred)
                sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
                st.pyplot(fig)
            
            with col_b:
                st.write("**Classification Report**")
                report = classification_report(y_true, y_pred, output_dict=True)
                st.dataframe(pd.DataFrame(report).transpose())

        except Exception as e:
            st.error(f"Error: {e}. Ensure the CSV format matches the training data.")

else:
    st.info("Please upload a CSV file to begin.")