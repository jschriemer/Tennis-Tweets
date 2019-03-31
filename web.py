#requests preforms http requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing

import re

#Python library for accessing the Twitter API
import tweepy

from urllib.request import urlopen #this module lets us grab web pages.
#note the would be just 'from urllib' in python 2.7
#BeautifulSoup handles HTML processing
from bs4 import BeautifulSoup #this module lets us easily parse the html.
#if you don't have BeautifulSoup downloaded, type 'pip install beautifulsoup4' into the command line

#Real link!!!
#tennis_ref = 'http://m.espn.com/general/tennis/dailyresults?wjb'
def get_score(auth, api):
    tennis_ref = 'http://m.espn.com/general/tennis/dailyresults?date=20190330&matchType=1&wjb='

    score_url = urlopen(tennis_ref)




    #Parse through site's html, and find class 'ind' (results stored here)
    tennis_score = BeautifulSoup(score_url, 'html.parser')
    game_section = tennis_score.findAll("div", class_="ind")


    #Seperates daily results into a list
    matches = []
    for line in game_section:
        if line.find(string = "Final"):
            word = line.text.split("Final")
            matches = matches + word

    count_match(matches, auth, api)

#counts number of daily matches
def count_match(matches, auth, api):
    count = 0
    for i in range(len(matches)):
        if matches[i]  != "":
            count = count + 1
    final_score(matches, count, auth, api)



#Splits lists results into strings and adds a space betwen score and players
def final_score(matches, count, auth, api):
    for i in range(len(matches)):
        if matches[i]  != "":
            score = re.sub(r'([a-z])(\d{1})', r'\1 \2', matches[i]) #split players and the score
            #player = re.find(r'([A-Z]\w+-*\w*)')
            #print(player.group(1) + player.group(2))
            api.update_status(score + " #tennis #atp #miamiopen")
