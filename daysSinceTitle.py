import os
import datetime
#import emailSender
import tweepy
import time
import sys
# sys.path.insert(1, '/Users/mac/Documents/PythonProjects/SMTP')

# Env variables
CONSUMER_KEY = os.environ.get('CONSUMER_KEY_TWITTER')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET_TWITTER')
ACCESS_KEY = os.environ.get('ACCESS_KEY_TWITTER')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET_TWITTER')

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    today = datetime.date.today()
    b = datetime.date(2014, 5, 31)
    diff = today - b
    days = diff.days

    print(days)
    try:
        api.update_status('{}'.format(days))
        print("Success")
    except Exception as err:
        print(err)
        '''emailSender.sendAlert(
            'ERR', 'Check Twitter pyBot on Raspberry Pi!', 'ondrejtichy07@gmail.com')'''
        pass

    time.sleep(86400)
