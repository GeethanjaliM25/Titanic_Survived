# 🚢 Titanic Survival Prediction App 🧠📊

A Machine Learning web application that predicts whether a passenger survived the Titanic disaster based on personal and travel details.  
Built using  **Python, Scikit-learn, and Streamlit**   
 
---

## 🛡️ Badges

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Dataset](https://img.shields.io/badge/Dataset-Titanic-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Project Overview

The **Titanic Survival Prediction App** uses the famous **Titanic dataset** to train a Logistic Regression model and predict survival outcomes.  
Users can input passenger details through a **Streamlit UI**, and the model returns survival prediction with probability.

---

## 🧾 Dataset Information

**Dataset Name:** Titanic-Dataset.csv  
**Source:** Kaggle Titanic Dataset  

### 📊 Features Used:
| Feature | Description |
|------|------------|
| Pclass | Passenger class (1st, 2nd, 3rd) |
| Sex | Gender of passenger |
| Age | Age (missing values handled) |
| Family | Total family members (SibSp + Parch) |
| Embarked | Port of embarkation (S, C, Q) |

### 🎯 Target Variable:
- **Survived** → 1 = Survived, 0 = Not Survived

---

## 🔧 Data Preprocessing Steps

- Filled missing **Age** with median
- Filled missing **Embarked** with most frequent value
- Dropped irrelevant columns:
  - PassengerId, Name, Ticket, Fare, Cabin
- Created new feature **Family**
- Encoded categorical variables:
  - Sex → Male = 1, Female = 0
  - Embarked → Label Encoding
- Limited age values to 54 (outlier handling)

---

## 🧠 Machine Learning Model

- **Algorithm:** Logistic Regression  
- **Train-Test Split:** 70% Train / 30% Test  
- **Library Used:** Scikit-learn  

The model predicts:
- Survival (Yes / No)
- Survival Probability (%)

---

## 🖥️ Application Interface (Streamlit)

Users can input:
- Passenger Class
- Gender
- Age
- Family Members
- Embarked Port

Click **"Predict Survival"** to get results.

---

## 🚀 Installation & Setup

###  Clone the Repository
```bash
git clone https://github.com/your-username/titanic-survival-prediction
cd titanic-survival-prediction

⭐ If you like this project, give it a star!
Made with ❤️ by Geethanjali M

