import os
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Suryansh")
    while True:
        x = input("Enter what you want me to speak: ")
        if (x == "q"):
            say('bye bye friend')
            break
        say(x)