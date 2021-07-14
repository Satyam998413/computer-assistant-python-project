# pip3 install pywin32 pypiwin32 pyttsx3
import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')#voices take uses
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[1].id)#for select jira voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak('Good Evening!')

    speak("I am Your Computer Assistant Please tell me how may I help You")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('spbaranwal9648@gmail.com', 'baranwal@998413')
    server.sendmail('spbarawal9648@gmail.com', to, content)
    server.close()



if __name__=="__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open udemy' in query:
            webbrowser.open("udemy.com")

        elif 'play music' in query:
            music_dir = 'E:\\music\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open vscode' in query:
            codePath = "C:\\Users\\spbar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open wpsoffice' in query:
            # codePath = "C:\Users\spbar\AppData\Local\Kingsoft\WPS Office\\ksolaunch"
            os.startfile(codePath)

        elif 'open autocad' in query:
            codePath ="C:\\Program Files\\Autodesk\\AutoCAD 2021\\acad"
            os.startfile(codePath)

        elif 'open chrom' in query:
            codePath ="C:\\Program Files\\Google\\Chrome\\Application\\chrome"
            os.startfile(codePath)
        
        elif 'open firefox' in query:
            codePath ="C:\Firefox\\X-Firefox"
            os.startfile(codePath)

        elif 'open edge' in query:
            codePath ="C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge"
            os.startfile(codePath)

        elif 'open cremenengineer':
            webbrowser.open("youtube.com/cremenengineer")

        elif 'email to satyam' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "satyambaranwalme998413@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Er. Satyam Baranwal. I am not able to send this email")