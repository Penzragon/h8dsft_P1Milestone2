import streamlit as st
import pickle
import pandas as pd
import requests
import random

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


def app():
    st.markdown(
        "<h1 style='text-align: center;'>π° Insurance Cost Prediction π°</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center;'>Simple insurance cost prediction using <strong>Polynomial Regression</strong>.</p>",
        unsafe_allow_html=True,
    )
    name = st.text_input("Name", "", placeholder="Enter your name")

    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", min_value=1, max_value=100)
    with col2:
        height = st.number_input("Height (cm)", min_value=1, max_value=300)

    col3, col4 = st.columns([1, 8])
    with col3:
        smoker = st.radio("Are you a smoker?", ("Yes", "No"))
    with col4:
        age = st.number_input("Age", min_value=1, max_value=100)

    bmi = weight / (height / 100) ** 2

    data = {"age": age, "bmi": bmi, "smoker": smoker.lower()}

    quotes = [
        "βAll the suffering, stress and addiction comes from not realising you already are what you are looking for.β β Jon Kabat-Zinn",
        "βYou are greater than your addiction.β β Nasia Davos",
        "βThe only way to get what you want is to work for it.β β Jim Rohn",
    ]

    quotes2 = [
        '"You do not buy life insurance because you are going to die, but because those you love are going to live." - Jim Rohn',
        '"If a child, a spouse, a life partner or a prent depends on you and your income, you need life insurance." - Suze Orman',
        '"Life insurance is a way to protect yourself from the unexpected." - Jeremiah',
    ]

    st.markdown("<hr>", unsafe_allow_html=True)

    col5, col6, col7 = st.columns([1.75, 1, 1])
    with col6:
        predict = st.button("Predict π§ ")

    if predict:
        with st.expander("See your prediction result π"):
            df = pd.DataFrame([data])
            prediction = model.predict(df)[0]
            name_ = name if name else "There"
            hi = f"<h1 style='text-align: center;'>Hi, {name_.title()}! π</h1>"
            charges = f"<h2 style='text-align: center;'>Your insurance charges are going to be: <br> <span style='color: #519259'>${prediction:,.0f}</span></h2>"
            st.markdown(hi, unsafe_allow_html=True)
            st.markdown(charges, unsafe_allow_html=True)
            if smoker.lower() == "yes":
                quote = (
                    f'<i><p style="text-align: center;">{random.choice(quotes)}</p></i>'
                )
                st.markdown(
                    '<br><p style="text-align: center;">π­Try to stop smoking to reduce you insurance chargesπ­</p>',
                    unsafe_allow_html=True,
                )
                st.markdown(quote, unsafe_allow_html=True)
            else:
                quote = f'<br><i><p style="text-align: center;">{random.choice(quotes2)}</p></i>'
                st.markdown(quote, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
