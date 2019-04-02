#Python library for accessing the Twitter API
import tweepy
import schedule
import time
from web import get_score


#api.update_status("The awesome text you would like to tweet")
def score_tweet():
    get_score(auth,api)


#def mainFunction():
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
    follower.follow()

schedule.every().day.at("23:59").do(score_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
