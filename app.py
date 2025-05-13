import streamlit as st
from PIL import Image
import base64

# ---------- Page Config ----------
st.set_page_config(page_title="Home of Innovation Chatbot", layout="centered")

# ---------- Background with CSS ----------
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

# ---------- Custom Font ----------
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"]  {
        font-family: 'Tajawal', sans-serif;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Logo ----------
logo = Image.open("static/logo.png")
st.image(logo, width=150)  # أكبر شوي

# ---------- Title ----------
st.markdown(
    "<h1 style='text-align: center; color: #000;'>Welcome to Home of Innovation Chatbot™</h1>",
    unsafe_allow_html=True
)

# ---------- Language Selection ----------
lang = st.radio("Language / اللغة", ["en", "ar"])

# ---------- User Input ----------
question = st.text_input("Ask a question / اطرح سؤالاً")

# ---------- Submit ----------
if st.button("Submit"):
    # Temporary placeholder response
    if lang == "en":
        text_response = "The Home of Innovation™ is a place and a program by SABIC to support Vision 2030."
    else:
        text_response = "موطن الابتكار™ هو مكان ومبادرة من سابك لدعم رؤية 2030."

    # ---------- Text Answer ----------
    st.markdown("### Text Response / الجواب نصاً")
    st.write(text_response)

    # ---------- Audio Response ----------
    st.markdown("### Audio Response / الجواب صوتاً")
    audio_file = "output.mp3"  # تأكدي أن ملف الصوت يتم حفظه بهذا الاسم
    st.audio(audio_file, format="audio/mp3", start_time=0)
