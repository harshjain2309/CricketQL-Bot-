import streamlit as st
from langchain_helper import get_ipl_db_chain

st.title("IPL Chatbot with SQL Query 🏏")

user_q = st.text_input("Ask any IPL-related question:")

if user_q:
    chain = get_ipl_db_chain()
    response = chain.run(user_q)
    st.subheader("Answer:")
    st.write(response)