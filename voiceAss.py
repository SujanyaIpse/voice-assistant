import speech_recognition as sr
import pyttsx3

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    # Add logic here to process commands and perform tasks
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "what is your name" in command:
        speak("I'm your voice assistant.")
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello! How can I help you?")
    while True:
        command = listen().lower()
        if "exit" in command:
            break
        process_command(command)
