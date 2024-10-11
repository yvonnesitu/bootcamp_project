# Set up and run this Streamlit App
import streamlit as st
from helper_functions import llm


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Resale flat prices")

with st.form("opt_form"):
    min = st.text_input("Minimum amount: ")
    max = st.text_input("Maximum amount: ")
    area = st.selectbox("Select preferred town", ["ANG MO KIO", "BEDOK", "BISHAN", "BUKIT BATOK", "BUKIT MERAH", "BUKIT PANJANG", "BUKIT TIMAH", "CENTRAL AREA", "CHOA CHU KANG", "CLEMENTI", "GEYLANG", "HOUGANG", "JURONG EAST", "JURONG WEST", "KALLANG/WHAMPOA", "MARINE PARADE", "PASIR RIS", "PUNGGOL", "QUEENSTOWN", "SEMBAWANG", "SENGKANG", "SERANGOON", "TAMPINES", "TOA PAYOH", "WOODLANDS", "YISHUN"])
    submit = st.form_submit_button("Search")

if submit:
    # Generate and display the DataFrame
    response_df = llm.generate_options(min, max, area)
    st.dataframe(response_df)