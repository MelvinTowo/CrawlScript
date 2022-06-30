import sys 
import tweepy #importing the twitter library
import pandas as pd
import csv
from pandas import ExcelWriter

consumer_key = 'Vi6xGbmMEjiLMpOvY4Bg87qFN'
consumer_secret = 'hyCYT7BviH6LKBG2Qp5RE8rJ7AkSzN0BNhwmof2XQoMPTtl4RM'
access_token = '2862438213-XNNBKMVkW4cnk7EK1S2t9HvtYMB8CqqvgiWOIbI'
access_secret = 'rM8w0g55F2kliGp7EotyJZ0Xj9bgniBuxC3BqefPoVN5M'
tweetsPerQry = 300 #number of results we recieve per request
maxTweets = 1000 #max number of tweets we want to recieve
hashtag = "trump" #Variable that we are searching for in twitter

#Twitter developer authentication
authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticate.set_access_token(access_token, access_secret)
api = tweepy.API(authenticate, wait_on_rate_limit = True) #wait on rate limit= auto sleep function
maxId = -1

#creating variables to hold specific tweet data from api
tweets = []
likes = []
time = []
location = []
userID = []

#asking api for queried results
for i in api.search_tweets(q = hashtag, count = tweetsPerQry, result_type="recent", tweet_mode= "extended"):
    tweets.append(i.full_text)
    # likes.append(i.favorite_count)
    time.append(i.author._json['created_at'])
    location.append(i.author._json['location'])
    userID.append(i.author._json['screen_name'])

#placing search results into a dataframe
df = pd.DataFrame({'twitter@': userID, 'tweets': tweets, 'location': location, 'time': time})
df.to_csv('results.csv')
writer = ExcelWriter('results.xlsx')
df.to_excel(writer)
writer.save()





