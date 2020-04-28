"""
Title: Tennis-Scores
Author: John Schriemer
Date: Created on March 24, 2019
License: MIT License
Description: Webscraping Twitter bot for Men's ATP tennis score retrieval.
"""
# pylint: disable=import-error
import time
import tweepy
import schedule
from web import get_score

#Twitter developer keys. See readme.md for more info


def score_tweet():
    """Get and post the tennis scores"""
    user = API.me()
    print(user.name)
    get_score(AUTH, API)


score_tweet()
#Automated posting at 11:59pm each day
#schedule.every().day.at("23:59").do(score_tweet)
#while True:
    #schedule.run_pending()
    #time.sleep(1)
