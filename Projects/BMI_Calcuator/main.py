# BMI calcuator using streamlit

import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kg :" , min_value=1.0, step=0.5) 
height = st.number_input("Enter your height in centimeters :" , min_value=1.0, step=0.5)
height_in_meters = height / 100
# Button to calculate BMI
if st.button("Calculate BMI"):
    if height_in_meters > 0:
        bmi = weight / (height_in_meters ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")



st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #34495e;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 10em;
    }
    </style>""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by Anamta</p>", unsafe_allow_html=True)


