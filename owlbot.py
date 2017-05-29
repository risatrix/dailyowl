from config import *

import json

import nltk
from nltk.tokenize.moses import MosesDetokenizer


import requests
import schedule
import time
import tweepy

def get_owl():
    # the base url to get the sortes text
    url = "http://api.aeneid.eu/sortes"

    r = requests.get(url)

    doc = r.json()
    raw_text = doc['text'][0]

    # break the sentence down into words, then parts of speech
    text = nltk.word_tokenize(raw_text)
    tokenized_list = nltk.pos_tag(text)

    # find a word the first noun so we can replace it
    replacement_index = ''
    for index, token in enumerate(tokenized_list):
        if token[1][:1] == 'N':
            replacement_index = index
            break

    #  replace that word with 'owl'
    text[replacement_index] = 'owl'

    # put the sentence back together again
    detokenizer = MosesDetokenizer()
    sentence = detokenizer.detokenize(text, return_str=True)
    print (sentence)

    # # get Twitter acess
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except:
        print("Error: Authentication failed")

    # tweet the owl sentence
    api.update_status(sentence)

schedule.every().day.at("08:30").do(get_owl)

while True:
    schedule.run_pending()
    time.sleep(1)

# add some emoji for fun
#test owl
# print(u'\U0001F989')
# #test chili peppers
# print(u"\U0001F336")
# print(u"\U000131B2")
