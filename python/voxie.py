import datetime
from bs4 import BeautifulSoup
import requests
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import pyautogui
import random
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 200)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + 0.50)

voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
def say(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    say("Ok sir , You can call me anytime")
                    break 
                elif "hello" in query:
                    say("Hello sir, how are you ?")
                    print(query)
                elif "i am fine" in query:
                    say("that's great, sir")
                elif "how are you" in query:
                    say("Perfect, sir")
                elif "thank you" in query:
                    say("you are welcome, sir")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)  
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    print(f"current{search} is {temp}")
                    say(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    print(f"current{search} is {temp}")
                    say(f"current{search} is {temp}")  
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    say(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                     say("Going to sleep,sir")
                     exit()
                elif "open" in query:
                     from Dictapp import openappweb 
                     openappweb(query)
                elif "close" in query:
                     from Dictapp import closeappweb 
                     closeappweb(query)
                elif "set an alarm" in query:
                     print("input time example:- 10 and 10 and 10")
                     say("Set the time")
                     a = input("Please tell the time :- ")
                     alarm(a)
                     say("Done,sir")
                elif "pause" in query:
                     pyautogui.press("k")    
                     say("video paused")
                elif "play" in query:
                     pyautogui.press("k")
                     say("video played")
                elif "mute" in query:
                     pyautogui.press("m")
                     say("video muted")

                elif "volume up" in query:
                     from keyboard import volumeup
                     say("Turning volume up,sir")
                     volumeup()
                elif "volume down" in query:
                     from keyboard import volumedown
                     say("Turning volume down, sir")
                     volumedown()     
                elif "remember that" in query:
                     rememberMessage = query.replace("remember that","")
                     rememberMessage = query.replace("jarvis","")
                     say("You told me to remember that"+rememberMessage)
                     remember = open("Remember.txt","a")
                     remember.write(rememberMessage)
                     remember.close()
                elif "what do you remember" in query:
                     remember = open("Remember.txt","r")
                     say("You told me to remember that" + remember.read())

                elif "news" in query:
                     from NewsRead import latestnews
                     latestnews()     
     

                
                    


        # sites = [["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"]]
        # for site in sites :
        #     if f"Open {site[0]}".lower() in query.lower():
        #         say(f"Opening {site[0]} Sir...")
        #         webbrowser.open(site[1])
        # if "play music" in query:
        #     musicpath= r"C:\Users\ADMIN\Downloads\Cheap-Thrills(PaglaSongs).mp3"
        #     os.system(f"start {musicpath}")
        # elif "the time" in query:
        #     time= datetime.datetime.now().strftime("%H:%M:%S")
        #     say(f"Sir the time is {time}")
        # elif "stop" in query:
        #     exit()
          # db=pymysql.connect(host="localhost" , user="root", password="komal@#6240)
          # mycursor=db.cursor()
          # mycursor.execute("show databases")
          # for db in mycursor:
          #     print(db)