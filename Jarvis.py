import requests
from bs4 import BeautifulSoup
import pyttsx3
import requests
from bs4 import BeautifulSoup




r = requests.get('https://www.ndtv.com/top-stories')
soup = BeautifulSoup(r.text,'lxml')

titles = soup.find_all('div')
for i in titles:
    links = soup.find_all('div',{'class' : 'nstory_header'})


f1 = open('C://Users//amitk//Desktop//Daily_News.txt', 'w')

for i in range(0,10):

        first_result = links[i]
        f1.write("\n")
        f1.write(str(i+1))

        f1.write(first_result.find('a').text)\


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


