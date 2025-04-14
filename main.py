import cohere
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get your API key from environment variable
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
cohere_client = cohere.Client(COHERE_API_KEY)

# Initialize speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen_and_generate_response():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")

        response = cohere_client.generate(
            prompt=f"Respond in one clear, concise sentence: {query}",
            max_tokens=50,
            temperature=0.7
        )

        generated_text = response.generations[0].text.strip()
        print(f"Response: {generated_text}")

        engine.say(generated_text)
        engine.runAndWait()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    listen_and_generate_response()
