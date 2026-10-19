"""Simple Interest Calculator
Devlop a Streamlit application that accepts Principal Amount, Rate of Interest
and Time Period from the user.
Provide a Calculate button to calculate and display the Simple Interest.
"""

import streamlit as st

st.title("Marvellous Infosystem")

st.header("Marvellous Even Or Odd Detector")

PA = st.number_input("Enter The Principal Amount", value=0, step=1)    #step allows a increment option on ui
IR = st.number_input("Enter The Rate Of Interest", value=0, step=1)
TP = st.number_input("Enter The Time Period (In Years)", value=0, step=1)    #step allows a increment option on ui

if st.button("Check"):
    interest = (PA * IR * TP)/100

    st.success("Simple Interest is : "+ str(interest))