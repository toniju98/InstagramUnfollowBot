# InstagramUnfollowBot

This project is another scraper that can show you which people you follow on instagram but don't follow you back. It was an idea when I had an instagram page and tried the strategy to follow
many people and after that unfollow the ones which didn't follow me back after some time.
So I decided to create this bot.

It is created with python. Important packages were Selenium for all the clicking actions and BeatifulSoap for Scraping

How does it work?

1. Login process (like in the other project)

2. Go on own profile

3. Go on follower list

4. Scroll through whole list and save all names in a list

5. Do the same with the followed list

6. Compare the trough lists and filter the people out who don't follow

IMPORTANT NOTE: HTML tags of web pages change with time, so you need to update them always