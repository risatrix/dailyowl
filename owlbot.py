import os
import json
import nltk
from nltk.tokenize.moses import MosesDetokenizer
import requests
import schedule
import time
import tweepy


consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')


# to ensure that the sentence ends with !?.
def repunctuate(str):
    punctuation = ",-:;' "
    translator = str.maketrans({key: "." for key in punctuation})
    new_str = str.translate(translator)
    return new_str

def get_owl():
    # the base url to get the sortes text
    url = "http://api.aeneid.eu/sortes"

    r = requests.get(url)

    doc = r.json()
    raw_text = doc['text'][0]

    # break the sentence down into words, then parts of speech
    text = nltk.word_tokenize(raw_text)
    tokenized_list = nltk.pos_tag(text)

    # find the first noun so we can replace it
    replacement_index = ''
    for index, token in enumerate(tokenized_list):
        if token[1][:1] == 'N':
            replacement_index = index
            break

    #  replace that word with 'owl'
    if replacement_index == 0:
        #capitalize if first word
        text[replacement_index] = 'Owl'
    else:
        text[replacement_index] = 'owl'

    # put the sentence back together again
    detokenizer = MosesDetokenizer()
    sentence = detokenizer.detokenize(text, return_str=True)
    # replace non-final punctuation
    punct = sentence[-1:]
    punct = repunctuate(punct)
    sentence = sentence[:-1]
    new_sentence = sentence + punct

    print (new_sentence)
    return new_sentence


def make_tweet(str):
    # get Twitter acess
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except:
        print("Error: Authentication failed")

    # tweet the string
    api.update_status(str)


def tweet_owl():
    tweet = get_owl()
    make_tweet(tweet)


get_owl()
# schedule.every().day.at("08:30").do(tweet_owl)
# schedule.every().day.at("12:30").do(tweet_owl)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

