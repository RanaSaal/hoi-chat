import streamlit as st
from gtts import gTTS
import tempfile
import os

# إعداد الصفحة
st.set_page_config(page_title="موطن الابتكار - سابك", layout="centered")

# الخط وتنسيق CSS
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"]  {
        font-family: 'Tajawal', sans-serif;
        background-image: url('static/background.png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .main-container {
        background-color: rgba(255, 255, 255, 0.88);
        padding: 3rem;
        border-radius: 20px;
        text-align: center;
        max-width: 750px;
        margin: auto;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    h1 {
        color: #005CB9;
        font-weight: 700;
        font-size: 2.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# الشعار
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.image("static/logo.png", width=200)

# العنوان
st.markdown("<h1>مرحبًا بك في موطن الابتكار™</h1>", unsafe_allow_html=True)

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

# واجهة المستخدم
lang = st.radio("Language / اللغة", ["en", "ar"])
user_input = st.text_input("Ask a question / اطرح سؤالًا", "")

if st.button("Submit"):
    if user_input:
        response, audio_path = answer_question(user_input, lang)
        st.markdown(f"**{response}**")
        st.audio(audio_path, format='audio/mp3')
        # ملاحظة: Streamlit لا يدعم التشغيل التلقائي الكامل للصوت
        # لكن الملف يتم عرضه مع إمكانية الضغط للتشغيل
        os.remove(audio_path)
    else:
        st.warning("Please enter a question.")

st.markdown("</div>", unsafe_allow_html=True)

