"""Celsius to Fahrenheit Calculator
Devlop a Streamlit application that accepts temperature in Celsius.
Provide a COnvert Button to convert the entered temperature into Fahrenhite and display the result.
"""

import streamlit as st

st.title("Marvellous Infosystem")

st.header("Marvellous Even Or Odd Detector")

# name = st.text_input("Enter The Student's Name", value=0)    #step allows a increment option on ui
C_temp = st.number_input("Enter The Temperature in Celsius", value=0, step=1)

if st.button("Fahrenhite"):

    fahrenhite = (C_temp * (9/5)) + 32
    
    st.success("Temperature is : "+ str(fahrenhite))
