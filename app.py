import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import warnings

warnings.filterwarnings("ignore")

st.title("🛥️Titanic Survival Prediction🛥️")


@st.cache_data
def model():
    
    df = pd.read_csv("Titanic-Dataset.csv")
    df["Age"].fillna(df["Age"].median(), inplace=True)
    df["Embarked"].fillna("S", inplace=True)
    df.drop(columns=["PassengerId", "Name", "Ticket", "Fare", "Cabin"], inplace=True)
    df["Family"] = df["SibSp"] + df["Parch"]
    df.drop(columns=["SibSp", "Parch"], inplace=True)
    df["Sex"] = np.where(df["Sex"] == "male", 1, 0)
    le = LabelEncoder()
    df["Embarked"] = le.fit_transform(df["Embarked"])

    df["Age"] = np.where(df["Age"] > 54, 54, df["Age"])
    x = df.drop(columns=["Survived"])
    y = df["Survived"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    log = LogisticRegression(max_iter=1000)
    log.fit(x_train, y_train)

    return log
log = model()
st.sidebar.header("Enter Passenger Information")
pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
sex = st.sidebar.selectbox("Gender", ["Male", "Female"])
age = st.sidebar.slider("Age", 1, 54, 25)
family = st.sidebar.number_input("Family Members", 0, 10, 1)
embarked = st.sidebar.selectbox("Embarked", ["S", "C", "Q"])
sex = 1 if sex == "Male" else 0
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_map[embarked]
input_data = np.array([[pclass, sex, age, family, embarked]])
if st.button("Predict Survival"):
    prediction = log.predict(input_data)
    probability = log.predict_proba(input_data)[0][1] * 100

    if prediction[0] == 1:
        st.success("Passenger survived")
    else:
        st.error("Passenger not survived")