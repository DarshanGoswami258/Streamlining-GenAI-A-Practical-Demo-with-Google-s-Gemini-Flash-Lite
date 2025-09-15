
import google.generativeai as genai
import streamlit as st
import os

# Get API frm local env
key = os.getenv("GOOGLE_API_KEY")   

# Configure the Model
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# create a frontend UI
st.title('SIMPLE TEXT GENRATION')
st.header('This to test the gemini model as application')
prompt = st.text_input('Write your prompt here', max_chars=200)
if prompt:
    response = model.generate_content(prompt)
    st.write(response.text)