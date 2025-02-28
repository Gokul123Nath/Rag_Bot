import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("📄 AI-Powered Chatbot")

# PDF Upload section
st.subheader("Upload a PDF Document")
uploaded_file = st.file_uploader("Choose a PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Uploading and processing..."):
        response = requests.post(f"{API_URL}/upload/", files={"file": uploaded_file})
        st.success(response.json().get("message"))

# Chatbot interaction
st.subheader("Ask Questions")
query = st.text_input("Type your question here...")

if st.button("Ask"):
    with st.spinner('Processing...'):
        response = requests.post(f"{API_URL}/chat/", params={"query": query})
        answer = response.json().get("answer")
        st.write("**Answer:**", answer)


