import tweepy
from tweepy import OAuthHandler
import json


consumer_key = 'UPzfiO0xU6uVbE40g0p6Wc2dx'
consumer_secret = 'ZkwVodwJqRtQCFUD9pBOazjruhHZ9xz22lgjcam33pJBcm3yrN'
access_token = '948042243335585792-hB5Gk027bmWDP2STHCjeTiu2F2vPbf6'
access_secret = 'Cjp8UllNSCj2tTUCToo2yWK88FN3zEAPXlBXMDTU0vFcZ'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def process_or_store(tweet):
    print(json.dumps(tweet))


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
