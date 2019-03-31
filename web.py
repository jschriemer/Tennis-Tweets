#requests preforms http requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
#BeautifulSoup handles HTML processing
#from bs4 import BeautifulSoup

from urllib.request import urlopen #this module lets us grab web pages.
#note the would be just 'from urllib' in python 2.7
from bs4 import BeautifulSoup #this module lets us easily parse the html.
#if you don't have BeautifulSoup downloaded, type 'pip install beautifulsoup4' into the command line


tennis_ref = 'http://m.espn.com/general/tennis/dailyresults?wjb'

score_url = urlopen(tennis_ref)
#lets look at what is stored here:
print(score_url)




tennis_score = BeautifulSoup(score_url, 'html.parser')
#game_section = tennis_score.find(class_="ind")
game_section = tennis_score.findAll("div", class_="ind")
#todays_games = game_section.findAll('',{'class','ind'})
#print(tennis_score)
#print(todays_games)
#print(game_section)
for line in game_section:
   if line.find(string = "Final"):
       print(line.text)
           #if line.find(string = "("):



#final = game_section.find(string = "Final")
#print(final)





"""
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
        print("YES")
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):

    #Returns True if the response seems to be HTML, False otherwise.
    print("YES")
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):

    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.

    print(e)
"""
