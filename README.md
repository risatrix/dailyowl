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

## Fun with CLTK and Heroku!
Well, that was exciting. Here's what didn't work:
1. Using any Python install method in the post_compile hook. The console would say it was downloading the data, but after all was said and done there was not a trace of the cltk_data folder anywhere in Heroku-uploaded repo. Interestingly, if I used the same commands in the Python shell from within `heroku bash`, everything installed just fine.
2. Flat-out copying the compiled cltk_data folders into the repo. None of the subfolders under `model` would upload to heroku. Again, if I ran the python install commands from bash, or I ran git from bash, the folders would populate correctly.

My suspicion is that this has to do with write permissions or some such, but I'm not being paid to figure this out.

I tried creating the folders manually in post_compile and using git to clone the models data, and it worked, so I'm going with that for now.

