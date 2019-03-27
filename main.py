#Python library for accessing the Twitter API
import tweepy

#requests preforms http requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
#BeautifulSoup handles HTML processing
from bs4 import BeautifulSoup

def mainFunction():
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


def simple_get(url):

    #Attempts to get the content at `url` by making an HTTP GET request.
    #If the content-type of response is some kind of HTML/XML, return the
    #text content, otherwise return None.

    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):

    #Returns True if the response seems to be HTML, False otherwise.

    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
