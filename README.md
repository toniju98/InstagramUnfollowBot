# InstagramUnfollowBot

> This project is another scraper that can show you which people you follow on instagram but don't follow you back. It was an idea when I had an instagram page and tried the strategy to follow
many people and after that unfollow the ones which didn't follow me back after some time.
So I decided to create this bot to speed up the process.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
This project is another scraper that simply executes click-commands in instagram step by step. It first logs in, then opens the 'My follower' and 'Followed' sections and then scrapes the contents.
After that it compares the two lists and filters the ones that are missing in the 'MyFollower'. Then it saves it to a .txt file and iterates over the file and unfollows all users.


## Technologies Used
- Python
- Selenium
- BeautifulSoup


## Features

- get list of people that don't follow you, but you follow them
- get follower list in instagram
- automatic unfollowing



## Setup

You can run it with the command: python scraper_instagram.py.
It probably won't work because HTML tags change with time. It is from 2021.



## Project Status
Project is: _complete_


## Room for Improvement

Room for improvement:
- Update the html tags
- ...

To do:
- Update the html tags


## Acknowledgements
- This project was inspired by an instagram page I ran in that time



## Contact
Created by [@toniju98](https://github.com/toniju98) - feel free to contact me!
