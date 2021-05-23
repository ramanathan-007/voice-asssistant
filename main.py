import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from News import *




listener= sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
   try:
      with sr.Microphone() as source:
        print('listening...')
        voice= listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'expo' in command:
           command= command.replace('expo','')
           print(command)
   except:
       pass
   return command

def run_expo():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('Playing'+song+'in youtube')
        pywhatkit.playonyt(song)
    elif 'single' in command:
        talk("I'm happily single")
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print('TIME:',time)
        talk('The current time is'+time)
    elif 'who' in command:
        person=command.replace('who','')
        info=wikipedia.summary(person,3)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'news' in command:
        arr=news()
        for i in range(len(arr)):
            talk(arr[i])
            print(arr[i])
    else:
        talk('Please say the command again')

while True:
   run_expo()

