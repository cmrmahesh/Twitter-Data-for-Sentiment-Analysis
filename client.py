import tweepy
from tweepy import OAuthHandler
from tweepy import Cursor

def get_client():
	consumer_key = 'HdToAC1EbR9mbmrN06xv8fze9'
	consumer_secret = '1dpwPFs31CO7o6T0l18sS97T2dRjh069wReLsnOyckgLDmMamu'
	access_token = '1723046504-0PzFyZu1ZTzaC4eSNH0yieEPL8Hq1jPmipuY5FH'
	access_secret = '6JdwTW3sxP2VkO39P7hn1msyvAZ65tJQJrn8hCHmkKd6e'

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth)
	return api


def get_auth():
	consumer_key = 'HdToAC1EbR9mbmrN06xv8fze9'
	consumer_secret = '1dpwPFs31CO7o6T0l18sS97T2dRjh069wReLsnOyckgLDmMamu'
	access_token = '1723046504-0PzFyZu1ZTzaC4eSNH0yieEPL8Hq1jPmipuY5FH'
	access_secret = '6JdwTW3sxP2VkO39P7hn1msyvAZ65tJQJrn8hCHmkKd6e'

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	return auth