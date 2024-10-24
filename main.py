# Set up and run this Streamlit App
import streamlit as st

st.title("About us")

overview = '''<p>The web application offers a one-stop service on HDB resale flat buying procedures and resale price inquiries. It leverages the power of automation, web scraping, and data filtering to deliver user-friendly tools for those seeking up-to-date information for their purchase and prospective home buyers.</p>

        <p><h4>Use Case 1: Resale Flat Buying Procedure Chatbot</h4></p>

<p>Our Resale Flat Buying Procedure Chatbot is designed to guide users through the often complex steps involved in purchasing an HDB resale flat. Whether users are looking for information on eligibility criteria, necessary documents, or key milestones in the buying process, the chatbot is equipped to provide clear, accurate, and up-to-date information. By utilizing web scraping from the HDB website, the chatbot ensures that users have access to the most current guidelines and procedural information at their fingertips.</p>

    <p>Key Features:<br>
        - Real-time guidance on the step-by-step resale flat buying process<br>
        - Web scraping from the official HDB website for accuracy<br>
        - Instant responses to common questions about eligibility, documents, and timelines
    </p>

        <p><h4>Use Case 2: HDB Resale Flat Price Search</h4></p>

<p>For users interested in buying or selling resale flats, our HDB Resale Flat Price Search tool offers an efficient way to explore the market. Users can input specific search criteria, such as flat type or price range, and our platform filters transaction data (up to the past 12 months) to provide a customized list of resale flat prices. This feature is built on a data-driven model that enables users to view real-time prices, making it easier for them to make informed decisions on their flat purchase or sale.</p>

    <p>Key Features:<br>
        - Interactive search functionality for filtering HDB resale flat prices by flat type or price range<br>
        - Intuitive interface for easy navigation and data exploration
    </p>
'''

st.html(overview)