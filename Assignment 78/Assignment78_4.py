"""Student Result Calculator
Devlop a Streamlit application that accepts a student's name and marks in three subjects.
Calculate total marks, percentage and display whether the student has passed or failed
Consider 40 marks out of 100 as the minimum passing marks in each subject.
"""

import streamlit as st

st.title("Marvellous Infosystem")

st.header("Marvellous Even Or Odd Detector")

name = st.text_input("Enter The Student's Name", value=0)    #step allows a increment option on ui
M1 = st.number_input("Enter The Marks of 1st Subject", value=0, step=1)
M2 = st.number_input("Enter The Marks of 2nd Subject", value=0, step=1)
M3 = st.number_input("Enter The Marks of 3rd Subject", value=0, step=1)

failed = False
if st.button("Check"):
    if M1 < 40 or M2 < 40 or M3 < 40:
        failed = True
        st.error(f"{name} is failed in one or more subjects.")

    else:
        percentage = ((M1 + M2 + M3) / 300) *100
    
        st.success("Percentage are : "+ str(percentage))
