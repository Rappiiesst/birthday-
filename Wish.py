import os
import time
import random
import pyttsx3

# Sound engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 130)

name = input("🎂 Enter your friend's name: ")

ascii_art = [
    r"""
    🎂🎉  HAPPY BIRTHDAY  🎉🎂
     ____||____
    |~ ~ ~ ~ ~|
    | H B D 🎈|
    |_________|
    """,
    r"""
      ✨🎂✨
    ╔══╗──╔╗
    ║╚═╬══╣╚╦╦╦══╦══╗
    ║╔╗║╔╗║╔╬╣╔╗║══╣
    ║╚╝║╚╝║║║║╔╗╠══║
    ╚══╩══╩╝╚╩╝╚╩══╝
    """,
    r"""
    🎈🎈🎈
      🍰 Happy Birthday 🍰
      To the most special soul!
    🎉🎉🎉
    """
]

wishes = [
    f"🎉 {name}, janmadin mubarak ho! Tumhara din khushiyon se bhara rahe! 💫",
    f"🎂 Happy Birthday {name}! Tumhari life sweet ho jaise cake 🎂",
    f"🎁 {name}, har pal me muskaan rahe, har din me khushi rahe! 🌟",
    f"💐 Tumhari zindagi me sirf pyaar, sukh aur safalta aaye! 🎉",
    f"🌈 {name}, tumhe mile har wo khushi jiske tum haqdaar ho 💖",
]

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Infinite birthday loop
while True:
    os.system("clear")
    art = random.choice(ascii_art)
    print("\033[1;36m" + art + "\033[0m")
    
    wish = random.choice(wishes)
    print("\033[1;33m" + wish + "\033[0m")
    
    speak("Happy Birthday to you, " + name)
    
    time.sleep(3)
