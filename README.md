# Daily Dose of Reddit
## Purpose

### This project was made for the UCSD 2022 Hackathon SD Hacks. This is a solo project and the devpost submission for the project can be found here: 

## Overview
* This is a Python script that will send an email of the top images from a subreddit specified in the script
* Images in jpg or png format will be added to the email as attatchments
* The images are sequentially added based off of the "hot" sorting system in reddit

## External Libraries
*This script uses multiple external python libraries to run. They are:*
1. praw (Reddit's public API)
2. smptlib (for handling emailing)
3. requests (for processing images from https address)

## Usage Notes
* Since this script uses external libraries, they must be installed in the programms environment in order to run using pip.
* The script only runs when called manually, but can be automated to run daily using batch files or windows task scheduler
* A good tutorial for doing the above can be found here: https://www.geeksforgeeks.org/schedule-a-python-script-to-run-daily/

**Editing important variables:**
You must edit various variables in the script to configure it to work for your email. These variables are all in a clearly marked section called _VARIABLES USER MUST EDIT_ in the code. The variables you *MUST* change are:
1. ```email```: the email that the images will be sent from. Make sure this isn't an important email, since you need weak security settings configured on it for the script to use it. As a note, you have to enable "less secure app access" from your account profile and not have 2 factor authentication on the email for the account to work.
2. ```password```: the password to the above email
3. ```TO```: the email you want images to be sent to

There are also other variables that are optional to edit to change settings:
1. ```subreddit_name```: the name of the subreddit for the script to search (default animemes)
2. ```image_amount```: the amount of images that will be sent in the email (defualt 10)
3. ```subject```: the subject of the email the script sends (default set to "Daily Dose of r/subreddit_name")


