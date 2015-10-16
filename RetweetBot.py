#!/usr/bin/env python
"""
Created on Fri Oct 16 22:25:07 2015

@author: Sladjana
@app name: BaskerBot
"""

import tweepy
import pandas as pd

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '' #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '' #keep the quotes, replace this with your access token
ACCESS_SECRET = '' #keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

results = api.search(q = 'datascience', count = 100)

ids = [a.id for a in results]
favs = [a.favorite_count for a in results]
retwts = [a.retweet_count for a in results]
txts = [a.text for a in results]
auths = [a.author.screen_name for a in results]

tw_df = pd.DataFrame({'id': ids,
                      'faved': favs,
                      'retweeted': retwts,
                      'text': txts,
                      'author':auths})

idx_rt_max = tw_df['retweeted'].idxmax()
idx_fav_max = tw_df['faved'].idxmax()

most_retweeted_id = tw_df.iloc[idx_rt_max].id
most_faved_id = tw_df.iloc[idx_fav_max].id

# Retweet!

api.retweet(most_retweeted_id)
if most_faved_id != most_retweeted_id:
    api.retweet(most_faved_id)
