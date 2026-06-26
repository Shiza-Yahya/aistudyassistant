from dotenv import load_dotenv
import os
from groq import Groq
import streamlit as st


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
print(api_key)  
client = Groq(api_key=api_key)
st.title(" My Study Assistant")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
user_input = st.chat_input("Ask Anything...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)