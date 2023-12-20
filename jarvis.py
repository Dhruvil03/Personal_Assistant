#importing required libraries
#if these libraries are not installed than run the following code in command prompt
#pip install pyttsx3
#pip install SpeechRecognition
#pip install wikipedia
#pip install PyAudio

import pyttsx3
import webbrowser
import wikipedia
import speech_recognition as sr
import datetime
import os
import sys

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

def speak(audio):      #  helps to communicate laptop with us
    engine.say(audio)  #  say method on the engine that passing input text to be spoken
    engine.runAndWait()
def wishme(datetime):
    hour = int(datetime.datetime.now().hour)         # taking current hour from current time
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak("Hey Dhruvil, jarvis here, please let me know how can I help you")

def takecommand():
    #it take a microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said:",query)
    except Exception as e:
        print(e)
        speak("say that again please...")
        return "none"
    return query

if __name__ == '__main__':             #starting of the program
    wishme(datetime)

    if 1:
        query = takecommand().lower()      #convert query into lowercase.
        if 'wikipedia' in query:
            speak("searching for wikipedia...please wait for a while")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)  # speak/return information of first two lines
            speak("According to, wikipedia")
            print(results)
            speak(results)

        #few functions of Jarvis
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open calendar' in query:
            webbrowser.open("calendar.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%h:%m:%S")
            speak(f'the time is{strTime}')

        elif 'no thanks' in query:
            speak("Thank you for using me. Have a good day")
sys.exit()

# I created an AI personal assistant named Jarvis using python.
#
#
# Jarvis can perform following tasks:-
#   * Search information on wikipedia.
#   * Open youtube.
#   * Open google.
#   * Open notepad.
#   * Open command prompt.
#   * Open stackoverflow.
#   * Open calendar.
#   * Speak current time.