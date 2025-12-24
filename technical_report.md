# Technical Report – Customer Churn Prediction

## 1. Introduction
This report documents the technical implementation of the Customer Churn Prediction capstone project. The objective is to build an end-to-end machine learning pipeline capable of predicting customer churn and supporting data-driven business decisions.

---

## 2. Dataset Description
**Dataset:** customer_churn.csv  

**Target Variable:**  
- `churn` (Binary: 1 = Churn, 0 = Retained)

**Features:**
- tenure
- monthlycharges
- totalcharges
- contract
- paymentmethod
- paperlessbilling
- seniorcitizen

The `customerid` column was removed as it is a unique identifier and does not contribute to prediction.

---

## 3. Data Preprocessing
- Column names standardized to lowercase
- `totalcharges` converted to numeric values
- Rows with missing values dropped
- Categorical variables encoded using Label Encoding
- Dataset split into training and testing sets using stratified sampling

---

## 4. Exploratory Data Analysis
Key observations from EDA:
- Customers with lower tenure show significantly higher churn
- Month-to-month contracts are strongly associated with churn
- Higher monthly charges increase churn probability
- Churn distribution is moderately imbalanced

EDA results guided feature importance interpretation and business recommendations.

---

## 5. Model Development

### 5.1 Baseline Model
**Logistic Regression**
- Used as a baseline for performance comparison
- Features scaled using StandardScaler
- Evaluation Metrics:
  - Recall
  - ROC-AUC

### 5.2 Final Model
**Random Forest Classifier**
- Selected due to better handling of non-linearity
- Class imbalance handled using `class_weight="balanced"`
- No feature scaling required
- Demonstrated improved recall and ROC-AUC compared to baseline

---

## 6. Model Evaluation
Evaluation techniques used:
- Recall (Primary Metric)
- ROC-AUC (Secondary Metric)
- Confusion Matrix
- Feature Importance Analysis

Random Forest achieved superior performance in identifying churn customers, reducing false negatives compared to the baseline model.

---

## 7. Feature Importance
Key features influencing churn:
- tenure
- contract
- monthlycharges
- totalcharges

Feature importance was used to derive actionable business insights.

---

## 8. Deployment Preparation
- Trained model serialized using Joblib
- Flask-based REST API created for real-time churn prediction
- End-to-end inference pipeline validated locally
- Deployment focused on functional demonstration rather than cloud hosting

---

## 9. Limitations
- Dataset size is limited
- No real-time customer behavior data included
- Label Encoding may impose artificial ordering on categorical variables

---

## 10. Conclusion
The project successfully demonstrates an end-to-end machine learning workflow. The final model is interpretable, deployable, and aligned with real-world business needs, making it suitable for academic evaluation and entry-level industry roles.
