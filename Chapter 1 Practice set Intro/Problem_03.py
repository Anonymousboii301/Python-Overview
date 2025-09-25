

# https://pypi.org/project/pyttsx3/
#  Module for text to speech in python 

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text...................................")
engine.runAndWait()