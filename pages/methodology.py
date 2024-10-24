# Set up and run this Streamlit App
import streamlit as st

st.title("Methodology")

c1 = st.container(border=True)
c1.header("Flow chart for use case 1")
c1.subheader("Resale Flat Buying Procedure Chatbot")
c1.image("use_case_chatbot.jpg")

c2 = st.container(border=True)
c2.header("Flow chart for use case 2")
c2.subheader("Resale Flat Prices")
c2.image("use_case_price_check.jpg")