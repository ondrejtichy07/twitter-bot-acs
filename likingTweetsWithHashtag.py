import tweepy
import csv
import pandas as pd
import os

# input your credentials here
# Env variables

CONSUMER_KEY = os.environ.get('CONSUMER_KEY_TWITTER')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET_TWITTER')
ACCESS_KEY = os.environ.get('ACCESS_KEY_TWITTER')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET_TWITTER')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

for tweet in tweepy.Cursor(api.search, q="#SKSlavia", count=100,
                           lang="en",
                           since="2019-01-01").items():
    print(tweet.created_at, tweet.text)
