# 🏦 Bank Marketing Prediction (Term Deposit Subscription)

## 📌 Overview

This project focuses on predicting whether a customer will subscribe to a **term deposit** based on bank marketing campaign data. The goal is to build a machine learning model that helps banks optimize their marketing strategies by identifying potential customers.

---

## 🎯 Objectives

* Perform **Exploratory Data Analysis (EDA)** to understand customer behavior
* Handle categorical and numerical features effectively
* Build and compare multiple classification models
* Evaluate performance using appropriate metrics
* Identify key factors influencing customer decisions

---

## 📊 Dataset Description

The dataset contains information related to direct marketing campaigns conducted by a bank.

### 🔑 Features Include:

* **Demographics**: age, job, marital status, education
* **Financial Info**: balance, housing loan, personal loan
* **Contact Info**: contact type, month, day
* **Campaign Info**: duration, campaign, previous outcomes

### 🎯 Target Variable:

* `y` →

  * `yes` (Subscribed)
  * `no` (Not Subscribed)

---

## 🔍 Exploratory Data Analysis (EDA)

* Checked missing values and data types
* Visualized categorical distributions (job, education, etc.)
* Analyzed numerical features (age, balance)
* Examined target distribution (imbalanced dataset)
* Used correlation heatmaps and count plots

### 💡 Key Insights

* Dataset is **imbalanced** (more “no” than “yes”)
* Call **duration** strongly influences subscription
* Previous campaign success increases likelihood
* Certain job categories show higher conversion rates

---

## ⚙️ Data Preprocessing

* Converted categorical variables using **One-Hot Encoding**
* Handled class imbalance (if applied: SMOTE / class weights)
* Scaled numerical features using **StandardScaler**
* Split dataset using **train-test split (stratified)**

---

## 🤖 Models Implemented

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)

---

## 🏆 Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Random Forest       | 89%     |
| Gradient Boosting   | 87%     |
| Logistic Regression | 86%     |



### ✅ Best Model: Random Forest / Gradient Boosting

* Handles non-linear relationships
* Works well with mixed feature types
* Robust to noise

---

## 🔧 Hyperparameter Tuning

Used **GridSearchCV / RandomizedSearchCV** to optimize:

* Number of trees (`n_estimators`)
* Tree depth (`max_depth`)
* Learning rate (for boosting models)

---

## 📈 Model Evaluation

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### ⚠️ Important Note

Due to class imbalance, **precision and recall are more important than accuracy**.

---

## 🔍 Feature Importance

* **Duration** (most influential feature)
* **Previous outcome**
* **Balance**
* **Age and job category**

### 💡 Insight

Customer interaction features (like call duration) are stronger predictors than demographic features.

---

## 🧪 Error Analysis

* False positives: predicted “yes” but actually “no”
* False negatives: missed potential customers

### 💡 Insight

Reducing false negatives is crucial for maximizing marketing success.

---

## 🚀 Business Impact

* Helps banks target the **right customers**
* Reduces marketing costs
* Improves campaign conversion rate

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn

---

## 📂 Project Structure

```id="4kzb4u"
├── bank_marketing.csv
├── model_training.ipynb
├── model.pkl
├── scaler.pkl
├── README.md
```

---

## 🔮 Future Improvements

* Use advanced models (XGBoost, LightGBM)
* Apply feature engineering (interaction features)
* Deploy model using Flask / FastAPI
* Add real-time prediction dashboard

---

## 📌 Conclusion

This project demonstrates how machine learning can be used to improve marketing strategies in banking. By identifying key factors influencing customer decisions, the model enables more targeted and efficient campaigns.

---

## 👤 Author

**Vrund Patel**
Aspiring AI Engineer | Machine Learning Enthusiast
