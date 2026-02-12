
# Bank-Marketing-Campaign-Prediction-A-Comparative-ML-Study
**ML Assignment 2 - BITS Pilani**

## 📌 Project Overview
This project implements an end-to-end Machine Learning workflow to predict if a bank customer will subscribe to a term deposit. The goal is to compare multiple classification algorithms and deploy the best performing model via an interactive Streamlit web application.

## 📊 Dataset Description
- **Source:** [UCI Machine Learning Repository - Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing)
- **Instances:** 41,188
- **Features:** 20 (demographic data, social/economic indicators, and campaign details)
- **Target Variable:** `y` (Has the client subscribed to a term deposit? Yes/No)

## 🛠️ Models Implemented
As per the assignment requirements, the following six classification models were built and evaluated:
1. Logistic Regression
2. Decision Tree Classifier
3. K-Nearest Neighbors (kNN)
4. Naive Bayes (Gaussian)
5. Random Forest (Ensemble)
6. XGBoost (Ensemble)

## 📈 Evaluation Metrics
Each model was evaluated using:
- Accuracy
- AUC Score
- Precision, Recall, and F1-Score
- Matthews Correlation Coefficient (MCC)

## 🚀 How to Run Locally
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/ML_Assignment_2_Classification.git
   cd ML_Assignment_2_Classification