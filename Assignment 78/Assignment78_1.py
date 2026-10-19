"""
Addition of Two Numbers
Devlop a Streamlit application that accepts two numbers from the user using input fields.
Provide an Add button to calculate and display the addition of entered numbers.
"""

import streamlit as st 
 
st.title("Marvellous Infosystem")

st.header("Marvellous Addition Calculator")

no1 = st.number_input("Enter First Number", value=0, step=1)    #step allows a increment option on ui
no2 = st.number_input("Enter Second Number", value=0, step=1)

if st.button("Addition"):
    result = no1 + no2

    st.success("Addition is : "+ str(result))