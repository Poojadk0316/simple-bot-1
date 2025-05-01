from dotenv import load_dotenv
import os
import google.generativeai as genai

# Force load from full path
load_dotenv(dotenv_path="C:/Users/Pooja D K/OneDrive/Desktop/python_2/.env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
