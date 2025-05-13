import streamlit as st
from gtts import gTTS
import tempfile
import os

# إعداد الصفحة
st.set_page_config(page_title="Home of Innovation Chatbot", layout="centered")

# تنسيق الواجهة
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"]  {
        font-family: 'Tajawal', sans-serif;
    }
    .stApp {
        background-image: url('static/background.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        padding: 2rem;
    }
    .custom-title {
        text-align: center;
        color: #005CB9;
        font-size: 2.8em;
        font-weight: bold;
        margin-top: 1rem;
    }
    .response-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# الشعار
st.image("static/logo.png", width=220)

# العنوان
st.markdown('<div class="custom-title">Welcome to Home of Innovation Chatbot</div>', unsafe_allow_html=True)

# اختيارات اللغة والسؤال
lang = st.radio("Language / اللغة", ["en", "ar"])
user_input = st.text_input("Ask a question / اطرح سؤالًا")
st.image("static/background.png", caption="هل الخلفية تظهر هنا؟")

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

# توليد الرد
if st.button("Submit"):
    if user_input:
        user_input_cleaned = user_input.lower().strip()
        response = qa_pairs.get(lang, {}).get(
            user_input_cleaned,
            "Sorry, I don't have an answer for that yet." if lang == "en" else "عذرًا، لا أملك إجابة لهذا السؤال حتى الآن."
        )

        # توليد الصوت
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts = gTTS(text=response, lang='en' if lang == 'en' else 'ar')
            tts.save(fp.name)
            audio_path = fp.name

        # عرض الرد النصي والصوتي
        st.markdown('<div class="response-box"><b>Answer:</b><br>' + response + '</div>', unsafe_allow_html=True)
        st.audio(audio_path, format='audio/mp3', start_time=0)

        # حذف الملف المؤقت
        os.remove(audio_path)
    else:
        st.warning("Please enter a question.")
