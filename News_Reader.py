import requests
from bs4 import BeautifulSoup
from Speak import *




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


