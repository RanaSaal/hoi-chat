import streamlit as st
from PIL import Image
from gtts import gTTS
import io
import base64

# ---------- Page Config ----------
st.set_page_config(page_title="Home of Innovation Chatbot", layout="centered")

# ---------- Background CSS ----------
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("static/background.png")

# ---------- Custom Font and Styles ----------
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"]  {
        font-family: 'Tajawal', sans-serif;
        color: #000000;
    }
    .title-small {
        font-size: 28px;
        text-align: center;
        color: #000;
        margin-bottom: 10px;
    }
    .section-label {
        font-size: 18px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 5px;
    }
    .response-box {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Logo ----------
logo = Image.open("static/logo.png")
st.image(logo, width=130)

# ---------- Title ----------
st.markdown("<div class='title-small'>Welcome to Home of Innovation Chatbot™</div>", unsafe_allow_html=True)

# ---------- Language Selection ----------
lang = st.radio("Language / اللغة", ["en", "ar"])

# ---------- User Input ----------
question = st.text_input("Ask a question / اطرح سؤالاً")

# ---------- Submit ----------
if st.button("Submit"):
    # Temporary placeholder response
    if lang == "en":
        text_response = "The Home of Innovation™ is a place and a program by SABIC to support Vision 2030."
        tts = gTTS(text_response, lang='en')
    else:
        text_response = "موطن الابتكار™ هو مكان ومبادرة من سابك لدعم رؤية 2030."
        tts = gTTS(text_response, lang='ar')

    # ---------- Text Answer ----------
    st.markdown("<div class='section-label'>Text Response / الجواب نصًا</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='response-box'>{text_response}</div>", unsafe_allow_html=True)

    # ---------- Audio Answer ----------
    st.markdown("<div class='section-label'>Audio Response / الجواب صوتًا</div>", unsafe_allow_html=True)
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    st.audio(audio_bytes, format="audio/mp3")

