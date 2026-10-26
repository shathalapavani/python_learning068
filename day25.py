import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
from urllib.parse import quote_plus

# Initialize
recogniser = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    with sr.Microphone() as mic:
        print("Listening...")
        recogniser.adjust_for_ambient_noise(mic, duration=0.5)
        audio = recogniser.listen(mic)

    try:
        text = recogniser.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except sr.UnknownValueError:
        speak("I am unable to understand. Please speak again.")
        return ""

    except sr.RequestError:
        speak("I am unable to connect to the service.")
        return ""

# Main program
speak("Hi, welcome to Voice Assistant. How can I help you?")

while True:
    command = listen()

    # Say hello
    if "hello" in command:
        speak("Hi, how can I help you?")

    # Tell current time
    elif "time" in command:
        curtime = datetime.now().strftime("%I:%M %p")
        speak("Current time is " + curtime)

    # Open Google
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Search on Google
    elif command.startswith("search"):
        search_text = command.replace("search", "", 1).strip()

        if search_text:
            speak("Searching for " + search_text)
            url = "https://www.google.com/search?q=" + quote_plus(search_text)
            webbrowser.open(url)
        else:
            speak("Please tell me what you want to search for.")

    # Exit assistant
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break