import streamlit as st
from gtts import gTTS
import tempfile
import os

# الأسئلة والإجابات
qa_pairs = {
    "en": {
        "what is home of innovation": "The Home of Innovation™ is a place and a program by SABIC to support Vision 2030.",
        "what is hoi": "The Home of Innovation™ is a place and a program by SABIC to support Vision 2030.",
        "where is home of innovation": "The Home of Innovation™ is located in Riyadh, Saudi Arabia.",
        "where is hoi": "The Home of Innovation™ is located in Riyadh, Saudi Arabia.",
        "what is sabic": "SABIC is a global leader in diversified chemicals headquartered in Riyadh, Saudi Arabia.",
        "how to visit hoi": "You can request a visit through the official SABIC Home of Innovation website.",
        "how to visit home of innovation": "You can request a visit through the official SABIC Home of Innovation website.",
        "can i visit home of innovation": "Yes, you can request a visit through the official website."
    },
    "ar": {
        "ما هو موطن الابتكار": "موطن الابتكار™ هو مبادرة من سابك لدعم رؤية المملكة 2030.",
        "اين يقع موطن الابتكار": "يقع موطن الابتكار™ في مدينة الرياض، المملكة العربية السعودية.",
        "ما هي سابك": "سابك هي شركة عالمية رائدة في مجال الكيماويات، مقرها الرياض.",
        "كيف يمكن زيارة موطن الابتكار": "يمكنك طلب زيارة عبر الموقع الرسمي لموطن الابتكار التابع لشركة سابك.",
        "هل يمكنني زيارة موطن الابتكار": "نعم، يمكنك تقديم طلب زيارة من خلال الموقع الرسمي."
    }
}

def answer_question(user_input, lang):
    user_input = user_input.lower().strip()
    responses = qa_pairs.get(lang, {})
    response = responses.get(user_input, "Sorry, I don't have an answer for that yet." if lang == "en" else "عذرًا، لا أملك إجابة لهذا السؤال حتى الآن.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts = gTTS(text=response, lang='en' if lang == 'en' else 'ar')
        tts.save(fp.name)
        audio_path = fp.name

    return response, audio_path

# إعداد الواجهة
st.set_page_config(page_title="موطن الابتكار - سابك", layout="centered")

# تدرج ألوان الخلفية + تنسيق مخصص
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #005CB9, #F47C20);
        color: white;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .custom-title {
        color: #005CB9;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .stTextInput>div>div>input {
        text-align: center;
    }
    .stRadio>div>label {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# عرض الشعار
st.image("static/logo.png", width=160)

# العنوان المخصص
st.markdown("<div class='custom-title'>Welcome to Home of Innovation™ Chatbot</div>", unsafe_allow_html=True)

lang = st.radio("Language / اللغة", ["en", "ar"])
user_input = st.text_input("Ask a question / اطرح سؤالًا", "")
if st.button("Submit"):
    if user_input:
        response, audio_path = answer_question(user_input, lang)
        st.write(response)
        st.audio(audio_path)
        os.remove(audio_path)
    else:
        st.warning("Please enter a question.")
