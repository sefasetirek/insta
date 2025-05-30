import openai
import streamlit as st

openai.api_key = st.secrets["openai"]["api_key"]

def generate_content(prompt, temperature=0.7, max_tokens=800):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']
