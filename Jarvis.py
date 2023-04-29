from datetime import datetime
from logging import exception
import os
import webbrowser
from click import command
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening!")
    speak("How may I help You Sir?!")

def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")
    except exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

if __name__=="__main__":
   wishME()
   while True :
    query = takeCommand().lower()
    
    #Search ------------->
    if 'wikipedia' in query:
        speak('searching Wikipedia...')
        query =query.replace("wikipedia"," ")
        results = wikipedia .summary(query ,sentences=2)
        speak("According to wikipedia")
        speak(results)

    elif 'search' in query:
        search = command.replace('search','')
        pywhatkit.search(search)    
    #---------------------->

    #open pages ----->
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')

    elif 'open google' in query:
        webbrowser.open('google.com')

    elif 'open stackoverflow' in query:
        webbrowser.open('stackoverflow.com')
    #------------------->

    #music ---------->
    elif 'play music' in query:
        music_dir ="D://"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'play the song' in query:
        song = command.replace('play the song','')
        speak ("playing"+song)
        pywhatkit.playonyt(song)
    #----------------->

    #time------------->
    elif 'the time' in query:
        strTime = datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    #------------------>

    #joke section------>
    elif 'date' in query:
        speak("sorry, I have a headache")
    elif 'are you single' in query:
        speak("I am in a relationship with wifi")
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    #--------------------->

    elif 'quit' in query:
        exit()
