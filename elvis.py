import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import pyjokes
from playsound import playsound
import pywhatkit
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis Your Assistant . Please Tell Me How May I Help You")
    
def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say That Again please.....")
        return "None"
    return query

if __name__ =="__main__":
      wishMe()
      while True:
       query = takeCommand().lower()

       if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

       if 'open youtube' in query:
           webbrowser.open("https://www.youtube.com/")

       if 'open facebook' in query:
           webbrowser.open("https://www.facebook.com/")

       if 'open instagram' in query:
           webbrowser.open("https://www.instagram.com/")

       if 'open twitter' in query:
           webbrowser.open("https://www.twitter.com/")

       if 'open meet' in query:
           webbrowser.open("https://meet.google.com/")

       if 'open amazon' in query:
           webbrowser.open("https://www.amazon.com/")

       if 'open flipkart' in query:
           webbrowser.open("https://www.flipkart.com/")

       if 'open stack overflow' in query:
           webbrowser.open("https://www.stackoverflow.com/")

       if 'open notepad' in query:
           npath = "C:\\windows\\system32\\notepad.exe"
           os.startfile(npath)

       if 'open vs code' in query:
           npath = "D:\\Microsoft VS Code\\code.exe"
           os.startfile(npath)

       if 'open codewithharry' in query:
           webbrowser.open("https://www.youtube.com/c/CodeWithHarry")

       if 'open whatsapp' in query:
           npath = "C:\\Users\\Rishit\\AppData\\Local\\WhatsApp\\whatsapp.exe"
           os.startfile(npath)

       if 'open my channel' in query:
           webbrowser.open("https://www.youtube.com/channel/UCB26bicxFQ92VdGjInENR8Q")

       if 'google search' in query:
           import wikipedia as googlescrap
           query = query.replace("jarvis","")
           query = query.replace("google search","")
           query = query.replace("google","")
           speak("This is what I found for your search")

           try:
               pywhatkit.search(query)
               result = googlescrap.summary(query,3)
               speak(result)

           except:
               speak("No speakable data found")

       if 'joke' in query:
           joke = pyjokes.get_joke()
           speak(joke)

       if 'set alarm' in query:
           speak("Sir Please Enter The Time!")
           time = input(": Enter Time :")

           while True:
               Time_Ac  = datetime.datetime.now()
               now = Time_Ac.strftime("%H:%M:%S")

               if now==time:
                   speak("Time To Wake Up Sir!")
                   playsound("alarm.mp3")

                   speak("Can you have any other work for me????")

       elif 'close' in query:
           speak("Ok Sir Thanks for using me have a good day")
           sys.exit()
        