#import required modules
import os
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
speak("Hello")