import requests
import sys
import tweepy
import urllib
import webbrowser

class TwitterAPI():

	def __init__(self): 
		print "Hello"
		consumer_key = "97GYp45AVZHBbLO2Ku80FKSoI"
		consumer_secret = "GUOrCYJCE1WosX3hlB1VdNkzGrBoks1Dzz824Zk8DZega3whMf"
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		access_token = "2956209245-ozCODTOUW9wz2kFYd3RdJxI8qP1trfoISqPPjHr"
		access_token_secret = "XwfpFr0vptElH47qWDJLKLABWxL0xVdfdtMQPVSlx0ud4"
		auth.set_access_token(access_token, access_token_secret)
		self.api = tweepy.API(auth)

	def test_tweet(self, message): 
		self.api.update_status(status=message)


class PocketAPI():

	def __init__(self): 
		self.consumer_key = "53266-0352132bef521461e927c48e"
		self.request_token = ""
		self.access_token = ""
		self.redirect_uri = "https://www.google.com"
		

def main(): 
	print "Hello world"
	twitter = TwitterAPI()
	pocket = PocketAPI()

	consumer_key = pocket.consumer_key
	url = pocket.redirect_uri
	payload = {'redirect_uri': url, 'consumer_key': consumer_key}
	r = requests.post('https://getpocket.com/v3/oauth/request', json=payload)
	print(r.text)
	pocket.request_token = r.text


	query = "https://getpocket.com/auth/authorize?"
	request_payload = {'request_token': pocket.request_token, 'redirect_uri': pocket.redirect_uri}
	query = query + urllib.urlencode(request_payload)	
	print(query)
	webbrowser.open_new(query)

if __name__ == '__main__':
    sys.exit(main())
	