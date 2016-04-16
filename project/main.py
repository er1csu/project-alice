import requests
import sys
import time
import tweepy
import urllib
import webbrowser

class TwitterAPI():

	def __init__(self): 
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

	s_request_url = "https://getpocket.com/v3/oauth/request"
	s_authorize_url = "https://getpocket.com/v3/oauth/authorize"
	s_request_authorization_url = "https://getpocket.com/auth/authorize?"
	s_get_url = "https://getpocket.com/v3/get"

	def __init__(self): 
		self.consumer_key = "53266-0352132bef521461e927c48e"	# Change per account 
		self.request_token = ""
		self.access_token = ""
		self.redirect_uri = "https://www.google.com"
		self.links = []
	
	def fetch_new_links(self): 
		pocket_list = requests.post(PocketAPI.s_get_url, data={'consumer_key': self.consumer_key, 
			'access_token': self.access_token, 'count': 5, 'detailType': "simple"})
		js_pocket_list = pocket_list.json() #dict
		for x in js_pocket_list['list'].itervalues(): 
			if ('given_url' in x): 
				self.links.append(x['given_url'])

	def initialize_pocket(self): 
		url = self.redirect_uri
		payload = {'redirect_uri': url, 'consumer_key': self.consumer_key}
		r = requests.post(PocketAPI.s_request_url, json=payload)
		self.request_token = r.text.split("=")[1]

		request_payload = {'request_token': self.request_token, 'redirect_uri': self.redirect_uri}
		query = PocketAPI.s_request_authorization_url + urllib.urlencode(request_payload)	
		webbrowser.open_new(query)

		time.sleep(5)
		r1 = requests.post(PocketAPI.s_authorize_url, json={'consumer_key': self.consumer_key, 
			'code': self.request_token})
		self.access_token = r1.text.split('&')[0].split('=')[1]



def main(): 
	twitter = TwitterAPI()
	pocket = PocketAPI()
	pocket.initialize_pocket()
	

	# Get list 
	pocket.fetch_new_links()
	


if __name__ == '__main__':
    sys.exit(main())
	