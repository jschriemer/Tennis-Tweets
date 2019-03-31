#Python library for accessing the Twitter API
import tweepy

from web import get_score

#def mainFunction():
consumer_key = 'nvNfiuecj0XCfgW1uaNkqR0kC'
consumer_secret = 'H3MobEXiwTOZvUUPCrsP17zDUJBGyIJKlLzW9bF18qdDCrMYHB'
access_token = '1109891876889473027-4dXciYX2pum8DLFGnYr8L7FgnFkmzj'
access_token_secret = 'ZuUWanATB0QAwxHxNtGBFRQwuCTp9AuAojGiFMNi8p7JB'
auth = tweepy.OAuthHandler('nvNfiuecj0XCfgW1uaNkqR0kC', 'H3MobEXiwTOZvUUPCrsP17zDUJBGyIJKlLzW9bF18qdDCrMYHB')
auth.set_access_token('1109891876889473027-4dXciYX2pum8DLFGnYr8L7FgnFkmzj', 'ZuUWanATB0QAwxHxNtGBFRQwuCTp9AuAojGiFMNi8p7JB')
api = tweepy.API(auth)


    #prints out Tennis_Scores
user = api.me()
print (user.name)

    #Auto Follow back any users that follow Tennis_Scores
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()


#api.update_status("The awesome text you would like to tweet")
get_score(auth,api)
