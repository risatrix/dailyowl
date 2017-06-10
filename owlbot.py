import os
import json
import nltk
from nltk.tokenize.moses import MosesDetokenizer
import requests
import schedule
import time
import tweepy

import cltk
from cltk.stem.latin.declension import CollatinusDecliner
from cltk.tag.pos import POSTag

consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')


decliner = CollatinusDecliner()
tagger = POSTag('latin')

# to ensure that the sentence ends with !?.
def repunctuate(str):
    punctuation = ",-:;' "
    translator = str.maketrans({key: "." for key in punctuation})
    new_str = str.translate(translator)
    return new_str


def get_data(url):
    r = requests.get(url)
    # parse the json response
    doc = r.json()
    raw_text = doc['text'][0]
    return raw_text


def get_owl():
    raw_text = get_data("http://api.aeneid.eu/sortes")

    # break the sentence down into words, then parts of speech
    text = nltk.word_tokenize(raw_text)
    tokenized_list = nltk.pos_tag(text)

    # find the first noun so we can replace it, and keep track of where it's at
    replacement_index = ''
    for index, token in enumerate(tokenized_list):
        if token[1][:1] == 'N':
            replacement_index = index
            break

    #  replace that word with 'owl' using the index
    if replacement_index == 0:
        #capitalize if first word
        text[replacement_index] = 'Owl'
    else:
        text[replacement_index] = 'owl'

    # put the sentence back together again
    detokenizer = MosesDetokenizer()
    raw_sentence = detokenizer.detokenize(text, return_str=True)
    sentence = clean_sentence(raw_sentence)
    print (sentence)
    return sentence

def get_latin_owl():
    raw_text = get_data("http://api.aeneid.eu/sortes?version=latin")

    # break down sentence into a list of words with syntax info
    tagger = POSTag('latin')
    tagged_sentence = tagger.tag_ngram_123_backoff(raw_text)

    # create an array showing the various forms of bubo with parts of speech
    decliner = CollatinusDecliner()
    declined_owl = decliner.decline("bubo")

    #create variables to collect the word to be replaced, and the replacement form
    replacement_str = ''
    commutandum = ''

    # loop through the list of tagged words
    for item in tagged_sentence:
        # some tags return None, hand with try/except
        try:
            #get the tag info
            syntax_str = item[1]
            # check the part of speech, number, and case
            if syntax_str[0] == 'N' and syntax_str[2] and syntax_str[7]:
                commutandum = item[0]
                number = syntax_str[2]
                case = syntax_str[7]
                # find the matching case and number for bubo
                for owl in declined_owl:
                    owl_syntax = owl[1]
                    if owl_syntax[2].capitalize() == number and owl_syntax[7].capitalize() == case:
                        replacement_str = owl[0]
                        print (owl[0])
                # stop after the first one, so we only replace one word
                break
            else:
                pass
        except:
            pass

    #replace the word
    raw_sentence = raw_text.replace(commutandum, replacement_str)
    sentence = clean_sentence(raw_sentence)
    print (sentence)
    return sentence

def clean_sentence(sentence):
    #replace non-final punctuation
    punct = sentence[-1:]
    punct = repunctuate(punct)
    sentence = sentence[:-1]
    new_sentence = sentence + punct

    print (new_sentence)
    return new_sentence


def make_tweet(str):
    # get Twitter access
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except:
        print("Error: Authentication failed")

    # tweet the string
    api.update_status(str)

get_owl()
get_latin_owl()

# def tweet_owl():
#     tweet = get_owl()
#     make_tweet(tweet)


# # schedule time  - 6 hrs = CST, also it uses 24-hr time
# schedule.every().day.at("13:30").do(tweet_owl)
# schedule.every().day.at("22:30").do(tweet_owl)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
