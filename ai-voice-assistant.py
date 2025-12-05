import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        return "Sorry, I didn't catch that."

def main():
    speak("Hello Wiem, I am your AI assistant!")
    while True:
        command = listen().lower()

        if "hello" in command:
            speak("Hello! How can I help?")
        elif "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("I am still learning.")

if __name__ == "__main__":
    main()
