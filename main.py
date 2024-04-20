import streamlit as st

st.title("Weather Forecast for the Week")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Conditions"))

st.subheader(f"{option} for the next {days} days in {place}")

