# Tennis Scores [![http://i.imgur.com/tXSoThF.png]][http://www.twitter.com/@TennisScores2]

Twitter bot that live tweets ATP & ITF tennis scores using python libraries ****Tweepy**** and ****BeautifulSoup****.

I created this because I am a tennis fan and because I wanted to learn more about internet bots and web scraping. Specifically, I was curious about how apps like Google Assistant pulled information automatically from other websites and wanted to try it myself.  These resources [baseball_scraping](https://gist.github.com/CNuge/ca6f6b3b257cf59124c87e3c8e7c5d88#file-ttib-baseball_scraping-ipynb), [Beautiful Soup](https://pypi.org/project/beautifulsoup4/), and [Tweepy](https://tweepy.readthedocs.io/en/v3.5.0/) were a big help during the process.
  ### 🎾🎾🎾
## Prerequisites
Install the libraries needed to run Tennis Scores. Tweepy is a python library for accessing the Twitter API, Request is for performing your HTTP requests, and BeautifulSoup4 for handling HTML processing. 
```bash
pip install tweepy requests beautifulsoup4
```
Create a twitter account to use for your bot on  [Twitter](https://twitter.com/signup). Youll have to apply to create a developer account, you can do that on their [developer site](https://developer.twitter.com/en.html). Once you have done so there are a few steps you need to take.
* Click 'Create an App'
* Provide the name and fill out the forms
* When finished, click 'Key and Access Tokens' to generate API keys

Once you have the API keys, you'll need them in your python file. 

```python
consumer_key = ''    
access_token = ''  
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)  
```
The next step is finding a site to use for the web-scraping portion. Use the 'inspect' feature on chrome to make sure it is easy to read the sites HTML. 
```python
website_url = 'website.com'
```
## Testing

Test Tweepy by printing your twitter username.

```python
api = tweepy.API(auth)
user = api.me()
print (user.name) 
```

Test Urlopen to see if the site can be opened.

```python
web_ref = urlopen(website_url)
print(web_ref)
  ```
Which should result in an HTTP response in the form of *<http.client.HTTPResponse object at 0x000000>*. 
Next, use BeautifulSoup to find the div section that holds the data you are trying to find.
```python
web_parser = BeautifulSoup(web_ref, 'html.parser')
desired_section_of_HTML = web_parser.findAll("div", class_="id_of_class")
print(desired_section_of_HTML)
```
Continue on from here using regular expressions to find the desired text (inside of  desired_section_of_HTML) that you wish to tweet. Once found you can use this command to create a tweet containing the found text.
```python
api.update_status(found_text)
 ```

## Documentation

[Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
[Tweepy](https://tweepy.readthedocs.io/en/v3.5.0/)

![alt text](http://cliparts.co/cliparts/Lid/jMy/LidjMy5dT.svg)
