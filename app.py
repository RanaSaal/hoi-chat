import streamlit as st
from gtts import gTTS
import tempfile
import os

# قاعدة الأسئلة والإجابات
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
        "ما هو موطن الابتكار": "موطن الابتكار هو مبادرة من سابك لدعم رؤية المملكة 2030.",
        "اين يقع موطن الابتكار": "يقع موطن الابتكار في مدينة الرياض، المملكة العربية السعودية.",
        "ما هي سابك": "سابك هي شركة عالمية رائدة في مجال الكيماويات، مقرها الرياض.",
        "كيف ازور موطن الابتكار": "يمكنك طلب زيارة عبر الموقع الرسمي لموطن الابتكار التابع لشركة سابك.",
        "كيف يمكنني زيارة موطن الابتكار": "يمكنك طلب زيارة عبر الموقع الرسمي لموطن الابتكار التابع لشركة سابك.",
        "كيف يمكن زيارة موطن الابتكار": "يمكنك طلب زيارة عبر الموقع الرسمي لموطن الابتكار التابع لشركة سابك.",
        "هل يمكنني زيارة موطن الابتكار": "نعم، يمكنك تقديم طلب زيارة من خلال الموقع الرسمي."
    }
}

# دالة للرد
from transformers import pipeline
fallback_model = pipeline("text-generation", model="gpt2")  # نموذج بسيط كمثال

def answer_question(user_input, lang, use_smart_reply=False):
    user_input = user_input.lower().strip()
    responses = qa_pairs.get(lang, {})
    response = responses.get(user_input)

    if not response and use_smart_reply:
        prompt = user_input if lang == 'en' else "Translate to Arabic and answer: " + user_input
        generated = fallback_model(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
        response = generated.strip()
    elif not response:
        response = "Sorry, I don't have an answer for that yet." if lang == 'en' else "عذرًا، لا أملك إجابة لهذا السؤال حتى الآن."

    tts = gTTS(text=response, lang='en' if lang == 'en' else 'ar')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio_path = fp.name

    return response, audio_path

# إعداد الصفحة
st.set_page_config(page_title="Home of Innovation Chatbot", layout="centered")

# الخلفية والتنسيق
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        background: url('static/background.png') no-repeat center center fixed;
        background-size: cover;
    }
    .response-box {
        background-color: rgba(255,255,255,0.85);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# عرض الشعار والعنوان
st.image("static/logo.png", width=200)
st.markdown("<h2 style='text-align:center; color:#005CB9;'>Welcome to Home of Innovation™ Chatbot</h2>", unsafe_allow_html=True)

# عناصر الواجهة
lang = st.radio("Language / اللغة", ["en", "ar"])
user_input = st.text_input("Ask a question / اطرح سؤالًا")
use_smart = st.checkbox("Use smart reply if no match found")
if st.button("Submit"):
    if user_input:
        response, audio_path = answer_question(user_input, lang, use_smart_reply=use_smart)
        st.markdown(f"<div class='response-box'><b>Answer (Text):</b><br>{response}</div>", unsafe_allow_html=True)
        st.markdown("<div class='response-box'><b>Answer (Audio):</b></div>", unsafe_allow_html=True)
        st.audio(audio_path)
        os.remove(audio_path)
    else:
        st.warning("Please enter a question.")
