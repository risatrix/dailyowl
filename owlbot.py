import requests
import nltk
import json

from nltk.tokenize.moses import MosesDetokenizer

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

# add some emoji for fun
#test owl
print(u'\U0001F989')
#test chili peppers
print(u"\U0001F336")
print(u"\U000131B2")
