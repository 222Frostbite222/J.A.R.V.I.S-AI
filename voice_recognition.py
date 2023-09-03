
# Import the required modules
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to voice input
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio)
    except OSError as e:
        print(f"No Default Input Device Available: {e}")
        print("Switching to text-based input for debugging...")
        return input("You: ")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()
