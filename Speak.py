import pyttsx3
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

engine.say("Hey Amit, ")
engine.say("Let's get into today's news. ")

with open('C://Users//amitk//Desktop//Daily_News.txt') as f:
    lines = f.read()
engine.say(lines)
engine.runAndWait()

