# Bank Marketing Campaign Prediction: A Comparative ML Study
**ML Assignment 2 - BITS Pilani**

## a. Problem Statement
The objective of this project is to predict whether a bank client will subscribe to a term deposit (target variable `y`) based on various attributes such as age, job, marital status, and previous marketing campaign outcomes[cite: 5, 28]. [cite_start]This is a binary classification problem aimed at identifying the most effective machine learning model to help the bank optimize its marketing strategy[cite: 9, 29].

## b. Dataset Description [1 mark]
- **Source:** [UCI Machine Learning Repository - Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing)[cite: 28].
- **Instances:** 4,521 (Meeting the minimum 500 requirement)[cite: 30].
- **Features:** 16 independent variables (Meeting the minimum 12 requirement)[cite: 30].
- **Target Variable:** `y` (Binary: 'yes' or 'no')[cite: 29].

## c. Models Used: [6 marks]
The following table provides a comparison of the evaluation metrics calculated for all 6 required models[cite: 32, 69, 70]:

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 89.39% | 0.8643 | 0.5294 | 0.1837 | 0.2727 | 0.2677 |
| **Decision Tree** | 87.29% | 0.6956 | 0.4220 | 0.4693 | 0.4444 | 0.3736 |
| **kNN** | 89.06% | 0.7451 | 0.4864 | 0.1836 | 0.2666 | 0.2512 |
| **Naive Bayes** | 82.65% | 0.8000 | 0.2993 | 0.4489 | 0.3591 | 0.2707 |
| **Random Forest (Ensemble)** | 90.16% | 0.9122 | 0.6000 | 0.2755 | 0.3776 | 0.3619 |
| **XGBoost (Ensemble)** | 89.72% | 0.9051 | 0.5352 | 0.3877 | 0.4497 | 0.4008 |

---

### Observations on Model Performance [3 marks]
Below are the performance observations for each implemented model[cite: 79, 80]:

| ML Model Name | Observation about model performance |
| :--- | :--- |
| **Logistic Regression** | Provides a strong accuracy baseline but suffers from low recall (18.37%), meaning it misses many potential subscribers. |
| **Decision Tree** | Captures non-linear relationships better than basic models, significantly improving the MCC (0.3736) and Recall (0.4693). |
| **kNN** | Performance is comparable to Logistic Regression in terms of accuracy, but it has the lowest MCC (0.2512), struggling with feature dimensionality. |
| **Naive Bayes** | Shows the lowest overall accuracy (82.65%) but maintains a decent recall, often over-predicting the minority class. |
| **Random Forest (Ensemble)** | Achieved the highest AUC (0.9122) and best overall Accuracy (90.16%), demonstrating high robustness. |
| **XGBoost (Ensemble)** | **Top Performer.** It achieved the highest MCC (0.4008) and a well-balanced F1-score, proving most effective at handling class imbalance. |

---

## 🛠️ Repository Structure
As per Step 3 requirements[cite: 50, 51]:
- `app.py`: Interactive Streamlit frontend[cite: 52].
- `requirements.txt`: List of dependencies (scikit-learn, pandas, etc.)[cite: 53, 56].
- `README.md`: Project documentation[cite: 54, 65].
- `model/`: Folder containing saved `.pkl` model files for all 6 implementations[cite: 55].

## 🚀 Deployment
- **Live App Link:** [Insert your Streamlit Cloud link here][cite: 19].
- **Platform:** Streamlit Community Cloud[cite: 20, 81].