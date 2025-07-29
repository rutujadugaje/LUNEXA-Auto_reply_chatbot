import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key = os.getenv('GEMINI_API_KEY'))


# def auto_reply_gemini_model():
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(' You are a person named Rutuja who speaks hindi as well as english. She is from India and is a coder. Respond in a friendly tone like Harry Potter.'
)
print(response.text)