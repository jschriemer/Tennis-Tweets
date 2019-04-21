"""
Title: Tennis-Scores
Author: John Schriemer
Date: Created on March 24, 2019
License: MIT License
Description: Webscraping Twitter bot for Men's ATP tennis score retrieval.
"""

import tweepy
import schedule
import time
from web import get_score



def score_tweet():
    get_score(auth,api)


#Twitter developer keys. See readme.md for more info
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')
api = tweepy.API(auth)


#prints out Tennis_Scores
user = api.me()
print (user.name)

#Auto Follow back any users that follow Tennis_Scores
for follower in tweepy.Cursor(api.followers).items():
#  if() #follower is NOT alreadey been followed by me,
   follower.follow()


score_tweet()

#Automated posting at 11:59pm each day
#schedule.every().day.at("23:59").do(score_tweet)
#while True:
    #schedule.run_pending()
    #time.sleep(1)
