# Your Daily Owl
A bot that tweets *sortes vergilianae*, but with owls.

## In More Detail
This bot visits the [Aeneid API's *sortes*](http://api.aeneid.eu/sortes) address to find a prophetic saying. Then it uses the NLTK to find the first noun in the
phrase and replaces it with the word 'owl'.

Why? Because I think the result is funny, and as informative as any other astrology bot you might want to consult.

## What the heck is a sortes?
The Sortes Virgilianae were a way of telling fortunes or answering questions by flipping to a random page of the *Aeneid*. If you don't believe me you can check the arbiter of internet truth, [Wikipedia](https://en.wikipedia.org/wiki/Sortes_Vergilianae). The Romans also practiced [augury by
birdwatching](https://en.wikipedia.org/wiki/Augury), so I thought the owl was in keeping with the general theme, in addition to being entertaining.

## TODOs
- [ ] add Latin owl tweets (need to upload CLTK to heroku for this)
- [ ] add reply functionality so you can get a personal response
- [ ] probably add emoji or something so it won't try to tweet the same things twice

