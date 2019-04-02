from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import tweepy


def get_score(auth, api):

    #Website url for webscraping
    tennis_ref = 'http://m.espn.com/general/tennis/dailyresults?wjb'
    score_url = urlopen(tennis_ref)

    #Parse through site's html, and find class 'ind' (results stored here)
    tennis_score = BeautifulSoup(score_url, 'html.parser')
    game_section = tennis_score.findAll("div", class_="ind")

    #create hashtag for current tournament
    tournament = tennis_score.find("div", class_="sec row")
    words = tournament.text
    length = len(re.findall(r'([A-Z]\w+-*\w*)', words))
    tourna = re.findall(r'([A-Z]\w+-*\w*)', words)

    tournament_tag = ''
    i = 0
    while(i < length):
        tournament_tag = tournament_tag + tourna[i]
        i = i + 1


    #Seperates daily results into a list
    matches = []
    for line in game_section:
        if line.find(string = "Final"):
            word = line.text.split("Final")
            matches = matches + word

    count_match(matches, auth, api, tournament_tag)

#counts number of daily matches
def count_match(matches, auth, api, tournament_tag):
    count = 0
    for i in range(len(matches)):
        if matches[i]  != "":
            count = count + 1
    final_score(matches, count, auth, api, tournament_tag)



#Splits lists results into strings and adds a space betwen score and players
def final_score(matches, count, auth, api, tournament_tag):
    for i in range(len(matches)):
        if matches[i]  != "":
            score = re.sub(r'([a-z])(\d{1})', r'\1 \2', matches[i])
            player = re.findall(r'([A-Z]\w+-*\w*)', score)

            api.update_status(score + " #tennis #atp #" + tournament_tag + " #" + player[0] + " #" + player[1])
