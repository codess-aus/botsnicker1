import tweepy
import time
import os
from flask import Flask, request
from twython import Twython
import random
from messages import messages
# from keys import * 

print('this is my twitter bot', flush=True)

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

twitter = Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET,
)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        message = random.choice(messages)
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#acswa' in mention.full_text.lower():
            print('found #acswa', flush=True)
            print('responding back...', flush=True)
            api.update_status('Hi ' '@' + mention.user.screen_name + ' ' + message, mention.id)
        elif '#snickers' in mention.full_text.lower():
            print('found #snickers', flush=True)
            print('responding back...', flush=True)
            api.update_status('Hi ' '@' + mention.user.screen_name + ' ' + message, mention.id)
        elif '#dddperth' in mention.full_text.lower():
            print('found #dddperth', flush=True)
            print('responding back...', flush=True)
            words = "The Robots are Rising at #DDDPerth " '@' + mention.user.screen_name
            # message = "Hello world - here's a pic!"
            image = open('dddperth1.png', 'rb')
            response = twitter.upload_media(media=image)
            media_id = [response['media_id']]
            #twitter.update_status(status=words, media_ids=media_id)
            api.update_status(status=words, media_ids=media_id)
        else:
            print('default response', flush=True)
            print('responding back...', flush=True)
            api.update_status('Hi ' '@' + mention.user.screen_name + ' You gotta use a hashtag to get an automated reply. Try #snickers ', mention.id)
        
while True:
    reply_to_tweets()
    time.sleep(15)

