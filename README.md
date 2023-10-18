# InstagramUnfollowBot

**InstagramUnfollowBot** is a web scraper project designed to help you identify Instagram users you follow but who do not follow you back. This project was born from a strategy I experimented with while managing an Instagram page. The idea was to follow a large number of people and then unfollow those who didn't reciprocate after some time. To streamline this process, I created this bot.

## Table of Contents
- [General Information](#general-information)
- [Technologies Used](#technologies-used)
- [Key Features](#key-features)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [Project Status](#project-status)
- [Room for Improvement](#room-for-improvement)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## General Information
**InstagramUnfollowBot** is a web scraper that automates actions on Instagram step by step. It begins by logging in, then accesses the 'My followers' and 'Followed' sections to scrape their contents. Next, it compares the two lists, filtering those users who are missing from the 'My Followers' list. The identified users are then saved to a .txt file, and the bot iterates over the file, unfollowing these users on Instagram.

## Technologies Used
- Python
- Selenium
- BeautifulSoup

## Key Features
- Get a list of people you follow but who don't follow you back
- Retrieve your follower list on Instagram
- Automate the unfollowing process

## Setup
You can run the bot using the following command: `python scraper_instagram.py`. However, please be aware that it may not work as expected due to changes in HTML tags over time. This code is from 2021.

## Project Status
Project Status: _Complete_

## Room for Improvement
Opportunities for improvement:
- Update the HTML tags to ensure compatibility with the latest Instagram structure

To-Do:
- Update the HTML tags

## Acknowledgements
This project was inspired by an Instagram page I managed at that time.

## Contact
Created by [@toniju98](https://github.com/toniju98) - Feel free to contact me!

