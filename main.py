import streamlit as st
import google.generativeai as genai
import os

# Get API Key from Secrets
api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

st.set_page_config(page_title="Myanmar AI Smart Chat", page_icon="🇲🇲")
st.title("🇲🇲 Myanmar AI Smart Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
