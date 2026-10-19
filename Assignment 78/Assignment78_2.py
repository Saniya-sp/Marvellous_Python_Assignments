"""Even or Odd number
Devlop a Streamlit application that accepts an integer from the user.
Provide a Check button to determine whether the entered number is even or odd and display the result.
"""

import streamlit as st

st.title("Marvellous Infosystem")

st.header("Marvellous Even Or Odd Detector")

no1 = st.number_input("Enter a Number", value=0, step=1)    #step allows a increment option on ui
# no2 = st.number_input("Enter Second Number", value=0, step=1)

if st.button("Check"):
    if no1 % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    st.success("The number is : "+ str(result))