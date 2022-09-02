import streamlit as st
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('model.h5')

st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)

st.title("Densification Predictor")

ss = st.number_input("Scan Spped (mm/s)")
hd = st.number_input("Hatch Distance (mm)")
lp = st.number_input("Laser Power (Watts)")
m = st.selectbox("Material",("IN718","Al-50%Si","AlSiMg0.75"))

if st.button("Submit"):
    if m=="IN718":
        m=2
    elif m=="Al-50%Si":
        m=0
    elif m=="AlSiMg0.75":
        m=1
    
    #X = np.array([m,ss,hd,lp])
    #X = X.astype(float)

    prediction = model.predict([[m,ss,hd,lp]])

    st.text(f"{prediction[0][0]}")

