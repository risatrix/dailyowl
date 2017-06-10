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
Well, that was as exciting I expected. Here's what didn't work:

1. Using any Python install method from within the `post_compile` hook.
When the hook ran during deployment, the console said it was downloading the data, but after all was said and done there was not a trace of the `cltk_data` folder anywhere in the Heroku repo. Fun!
Interestingly, if I used the individual Python commands from within the `heroku run bash` Python shell, everything installed just fine. If I created a separate Python install script file and ran it from the bash shell, it also worked just fine. Trying to do any of that from the post_compile hook? So much nope.

2. Running a Python install script from Heroku's CLI. That is, using my local terminal and running `heroku run python my_install_script.py`. Said it was running, but when I went back into the shell, no folder. Still more nope!

3. Flat-out copying the compiled cltk_data folders into the repo. (Yes, I know.)
When I uploaded the entire compiled `cltk_data` folder to Heroku, all subfolders under `model` disappeared. Again, if I ran the Python install commands from the shell in bash, or I used git to clone them from within bash, the subfolders would populate correctly.

This lead me using git from the `post_compile` script to clone the models data, and it worked. ¯\_(ツ)_/¯

I manually recreated the folder structure that cltk expects, and added it to the path in my main file, and that worked too.

My suspicion is that the pre-compile/upload issues have to do with write permissions or some such, but figuring that out is above my current pay grade. Better yet, someone who's getting paid can add CLTK to the Python buildpack! But definitely not me!
