import tweepy
import time
from PIL import Image
import wget
import sys
import os



consumer_key = "g1ixiQs7Rr0eGFZbt85reRcJJ"
consumer_secret = "UZnEC34bA0Nnazv6xHm5lx8ECKO453eHMTjOSfbo46AgUf2wAZ"
access_key = "2207663112-7bjBn3Rr9XEj9NJWboXuAlbK70era4yY5UsaAqi"
access_secret = "lXg4A8bmBGLjSh9tNNPD5WolndPZHnZYcEd6cf2XbS7xm"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
me = api.me()
tango = api.get_user(screen_name="OmarSy")
print(tango)
