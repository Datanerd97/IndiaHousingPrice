import streamlit as st
import joblib 
import numpy as np


    
# Load the model
model = joblib.load("model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learning for predicting house prices with given features of the house. For using this app you can enter input and predict your House Price")

st.divider()

bedrooms = st.number_input("Number of bedrooms",min_value = 0,value = 0)
bathrooms = st.number_input("Number of bathrooms",min_value = 0,value = 0)
livingarea = st.number_input("Living area",min_value = 0, value = 2000)
condition = st.number_input("Condition",min_value = 0, value = 3)
numberofschools = st.number_input("Number of schools nearby",min_value = 0,value = 0)
numberoffloors = st.number_input("Number of floors",min_value = 0,value = 0)

st.divider()

X = [[bedrooms,bathrooms,livingarea,condition,numberoffloors,numberofschools]]

predictbutton = st.button("Predict!")

if predictbutton:

    st.balloons()

    X_array = np.array(X)
    prediction = model.predict(X_array)[0]

    st.write(f"Price prediction is {prediction:,.2f}")

else:
    st.write("Please press predict after entering values")




