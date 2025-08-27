import streamlit as st
import random
from quotes import quotes  # Importing quotes database

# ============ RANDOM FONTS ============
fonts = [
    "Arial", "Georgia", "Courier New", "Verdana", 
    "Tahoma", "Trebuchet MS", "Comic Sans MS", "Lucida Console"
]
random_font = random.choice(fonts)

# ============ PAGE CONFIG ============
st.set_page_config(page_title="Random Quotes Generator", page_icon="💭", layout="centered")

# ============ CUSTOM CSS ============
st.markdown(
    f"""
    <style>
    body {{
        background-color: #E6E6FA; /* Lilac */
        text-align: center;
    }}
    .stApp {{
        background-color: #E6E6FA;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }}
    .quote-box {{
        font-family: '{random_font}', sans-serif;
        font-size: 28px;
        font-weight: bold;
        color: #4B0082; /* Indigo Purple */
        background-color: #ffffffdd;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        margin: auto;
        width: 80%;
        max-width: 700px;
    }}
    .stButton>button {{
        background-color: #800080;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #BA55D3;
        transform: scale(1.05);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ============ APP TITLE ============
st.markdown("<h1 style='color:#4B0082; font-family:Georgia;'>✨ Random Quotes Generator ✨</h1>", unsafe_allow_html=True)

# ============ TOPIC SELECTION ============
topic = st.selectbox("Choose a Topic", list(quotes.keys()))

# ============ RANDOM QUOTE ============
if st.button("🎲 Generate Quote"):
    selected_quote = random.choice(quotes[topic])
else:
    selected_quote = random.choice(quotes[topic])

# ============ DISPLAY ============
st.markdown(f"<div class='quote-box'>{selected_quote}</div>", unsafe_allow_html=True)
