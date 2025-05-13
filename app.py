import streamlit as st
from PIL import Image
from gtts import gTTS
import io
import base64

# إعداد الصفحة
st.set_page_config(page_title="Home of Innovation Chatbot", layout="centered")

# خلفية مخصصة
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

# الخط والتنسيقات
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        color: #000 !important;
    }
    .title-small {
        font-size: 28px;
        text-align: center;
        color: #000;
        margin-bottom: 10px;
    }
    .section-label {
        font-size: 14px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 5px;
        color: #000;
    }
    .response-box {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 10px;
        color: #000;
    }
    input[type="text"] {
        color: #000 !important;
    }
    .stTextInput label, .stRadio label {
        color: #000 !important;
    }

    /* 🔥 هذا السطر يحل مشكلة لون النص المحدد في الراديو */
    div[role="radiogroup"] > label > div {
        color: #000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# إخفاء Streamlit الافتراضي
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# الشعار
logo = Image.open("static/logo.png")
st.image(logo, width=220)

# العنوان
st.markdown("<div class='title-small'>Welcome to Home of Innovation Chatbot™</div>", unsafe_allow_html=True)

# اختيار اللغة
lang = st.radio("Language / اللغة", ["en", "ar"])

# قاعدة البيانات
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
        "اين موطن الابتكار": "يقع موطن الابتكار في مدينة الرياض، المملكة العربية السعودية.",
        "ما هي سابك": "سابك هي شركة عالمية رائدة في مجال الكيماويات، مقرها الرياض.",
        "كيف ازور موطن الابتكار": "يمكنك طلب زيارة عبر الموقع الرسمي لموطن الابتكار التابع لشركة سابك.",
        "كيف يمكنني زيارة موطن الابتكار": "يمكنك طلب زيارة عبر الموقع الرسمي لموطن الابتكار التابع لشركة سابك.",
        "كيف يمكن زيارة موطن الابتكار": "يمكنك طلب زيارة عبر الموقع الرسمي لموطن الابتكار التابع لشركة سابك.",
        "هل يمكنني زيارة موطن الابتكار": "نعم، يمكنك تقديم طلب زيارة من خلال الموقع الرسمي."
    }
}

# حقل السؤال
question = st.text_input("Ask a question / اطرح سؤالاً")

# عند الضغط على زر الإرسال
if st.button("Submit"):
    question_clean = question.strip().lower()
    answer = qa_pairs.get(lang, {}).get(
        question_clean,
        "Sorry, I don't have an answer for that yet." if lang == "en" else "عذرًا، لا أملك إجابة على هذا السؤال حاليًا."
    )

    st.markdown("<div class='section-label'>Text Response / الجواب نصًا</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='response-box'>{answer}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-label'>Audio Response / الجواب صوتًا</div>", unsafe_allow_html=True)
    tts = gTTS(answer, lang=lang)
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    st.audio(audio_bytes, format="audio/mp3")
    
    # زر تحميل الصوت (حل بديل في حال ما اشتغل)
    st.download_button(
        label="Download Audio / تحميل الصوت",
        data=audio_bytes,
        file_name="response.mp3",
        mime="audio/mp3"
    )


