import gradio as gr
from gtts import gTTS
import tempfile

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

# دالة الإجابة مع صوت
def answer_question(user_input, lang):
    user_input = user_input.lower().strip()
    responses = qa_pairs.get(lang, {})
    response = responses.get(user_input, "Sorry, I don't have an answer for that yet." if lang == "en" else "عذرًا، لا أملك إجابة لهذا السؤال حتى الآن.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts = gTTS(text=response, lang='en' if lang == 'en' else 'ar')
        tts.save(fp.name)
        audio_path = fp.name

    return response, audio_path

# تصميم الخلفية والشعار
background_style = """
<style>
body {
  background: linear-gradient(to bottom right, #005CB9, #F7931E);
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
}
h1 {
  color: white;
  text-align: center;
  font-weight: bold;
  font-size: 32px;
  margin-bottom: 20px;
}
.gradio-container {
  background: rgba(255, 255, 255, 0.95);
  padding: 30px;
  border-radius: 20px;
  margin: auto;
  max-width: 750px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
"""

logo_html = """
<div style="text-align: center; margin-bottom: 10px;">
  <img src='file/logo.png' width='160'>
</div>
"""

# واجهة Gradio
with gr.Blocks() as demo:
    gr.HTML(background_style + logo_html)
    gr.Markdown("# Welcome to the Home of Innovation™ Chatbot!", elem_id="main_title")

    with gr.Column():
        lang = gr.Radio(["en", "ar"], label="Language / اللغة")
        user_input = gr.Textbox(label="Ask a question / اطرح سؤالًا", placeholder="Example: What is Home of Innovation?")
        output_text = gr.Textbox(label="Answer")
        output_audio = gr.Audio(label="Voice", autoplay=True)
        btn = gr.Button("Submit")

    btn.click(fn=answer_question, inputs=[user_input, lang], outputs=[output_text, output_audio])

demo.launch()