import client 
import tweepy
import json
import sys
import string
from tweepy import Cursor
from tweepy import Stream
from tweepy.streaming import StreamListener


class CustomListener(StreamListener):
	# def __init__(self, query):
	# 	self.outfile = 'stream_%s.json' % (query)

	def on_data(self, data):
		try:
			with open('python.json','a') as f:
				f.write(data)
				#print(data)
				return True
		except BaseException as e:
			print("Error on_data: %s" %str(e))
			time.sleep(5)

		return True

	def on_error(self, status):
		print(status)
		return True

if __name__ == '__main__':
	api = client.get_client()

	auth = client.get_auth()

	query = sys.argv[1:]
	query_fname = ' '.join(query)
	twitter_stream = Stream(auth, CustomListener())
	twitter_stream.filter(track=['#python'], async=True)

	# with open('home_timeline.jsonl','w') as f:
	# 	for page in Cursor(client.home_timeline).pages(4):
	# 		for status in page:
	# 			f.write(json.dumps(status._json)+"\n")

