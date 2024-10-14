# Set up and run this Streamlit App
import streamlit as st
from helper_functions import llm

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="AI-Bootcamp Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Resale Flat Prices")
st.write("Check the resale prices for the past 12 months.")

# Get maximum price dynamically
max_price = llm.get_price()

with st.form("opt_form"):
    # Slider for selecting price range
    price_range = st.slider("Price range", 0, max_price, value=[100000, 500000], step=1000)

    # Multiselect for flat types
    flat_types = st.multiselect("Select preferred flat type", ["1 ROOM", "2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE", "MULTI-GENERATION"])

    # Selectbox for choosing area
    area = st.selectbox("Select preferred town", ["None", "ANG MO KIO", "BEDOK", "BISHAN", "BUKIT BATOK", "BUKIT MERAH", "BUKIT PANJANG", "BUKIT TIMAH", "CENTRAL AREA", "CHOA CHU KANG", "CLEMENTI", "GEYLANG", "HOUGANG", "JURONG EAST", "JURONG WEST", "KALLANG/WHAMPOA", "MARINE PARADE", "PASIR RIS", "PUNGGOL", "QUEENSTOWN", "SEMBAWANG", "SENGKANG", "SERANGOON", "TAMPINES", "TOA PAYOH", "WOODLANDS", "YISHUN"])

    # Submit button
    submit = st.form_submit_button("Search")

# Process form submission
if submit:
    min_price = price_range[0]
    max_price = price_range[1]

    # Validate inputs: at least one of area or price range should be provided
    if area == "None" and (min_price <= 0 and max_price <= 0):
        st.error("Please provide either a preferred town or a valid price range.")
    else:
        # Input validation for prices
        try:
            # Ensure min_price is less than or equal to max_price
            if min_price > max_price:
                st.error("Minimum amount must be less than or equal to maximum amount.")
            else:
                # Generate and display the DataFrame based on selected options
                response_df = llm.generate_options(min_price, max_price, area, flat_types)
                if response_df.empty:
                    st.warning("No results found for the selected criteria.")
                else:
                    st.dataframe(response_df)
        
        except ValueError:
            st.error("Please enter valid numeric values for minimum and maximum amounts.")
