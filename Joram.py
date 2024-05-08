import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

recognizer = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Function to greet the user based on the time of day"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    
    speak("I am your AI assistant. How may I assist you?")

def take_command():
    """Function to listen to user's voice command"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        statement = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {statement}")
        return statement.lower()
    except Exception as e:
        print(e)
        speak("What are you saying.")
        return ""

if __name__ == '__main__':
    wish_me()

    while True:
        speak("?")
        statement = take_command()

        if "goodbye" in statement or "exit" in statement:
            speak('Goodbye! Have a great day!')
            break

        elif "open notepad" in statement:
            os.system("notepad.exe")
            speak("Opening Notepad...")

        elif "open google" in statement:
            webbrowser.open("https://www.google.com")
            speak("Opening Browser...")
        
        elif "open youtube" in statement:
            webbrowser.open("https://www.youtube.com")
            speak("Opening Youtube...")
            
        elif "open stack overflow" in statement:
            webbrowser.open("https://www.stackoverflow.com")
            speak("Opening StackOverflow...")
            
        
        elif "open Opera" in statement:
            webbrowser.open("https://www.opera.com")
            speak("Opening Opera...")
            

        elif "open Gmail" in statement:
            webbrowser.open("https://www.gmail.com")
            speak("Opening Gmail...")
            
            
        elif "shutdown" in statement:
            os.system("shutdown /s /t 1")
            speak("Shutting down the system...")
            
        elif "shut down" in statement:
            os.system("shutdown /s /t 1")
            speak("Shutting down the system...")


        else:
            speak(" ")
