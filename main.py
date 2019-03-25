import tweepy
#Python library for accessing the Twitter API


consumer_key = 'nvNfiuecj0XCfgW1uaNkqR0kC'
consumer_secret = 'H3MobEXiwTOZvUUPCrsP17zDUJBGyIJKlLzW9bF18qdDCrMYHB'
access_token = '1109891876889473027-4dXciYX2pum8DLFGnYr8L7FgnFkmzj'
access_token_secret = 'ZuUWanATB0QAwxHxNtGBFRQwuCTp9AuAojGiFMNi8p7JB'
auth = tweepy.OAuthHandler('nvNfiuecj0XCfgW1uaNkqR0kC', 'H3MobEXiwTOZvUUPCrsP17zDUJBGyIJKlLzW9bF18qdDCrMYHB')
auth.set_access_token('1109891876889473027-4dXciYX2pum8DLFGnYr8L7FgnFkmzj', 'ZuUWanATB0QAwxHxNtGBFRQwuCTp9AuAojGiFMNi8p7JB')
api = tweepy.API(auth)

user = api.me()
print (user.name)
