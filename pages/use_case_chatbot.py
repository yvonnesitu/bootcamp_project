# Set up and run this Streamlit App
import streamlit as st
from helper_functions import llm

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="AI-Bootcamp Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Housing loan chatbot")

# initalize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:= st.chat_input("Enter your prompt here"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = llm.generate_response_to_query(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
