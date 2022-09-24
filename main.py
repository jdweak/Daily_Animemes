
from re import sub
import praw
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup as bs
import requests

#function to send email
def send_mail(email, password, FROM, TO, msg):
    # initialize the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # connect to the SMTP server
    server.starttls()
    # login
    server.login(email, password)
    # send the email
    errors = server.sendmail(FROM, TO, msg.as_string())
    # terminate the SMTP session
    server.quit()

# __________________________VARIABLES USER MUST EDIT____________________________________
# credentials for the email account sending the email. Be careful with this, as
# you are providing the credentials to login to an email. It is reccomended to
# do this from an alternate account to reduce any security concerns (this
# version of the script uses Google's updated app passwords model for
# authentication which is more secure, but better safe than sorry)

email = "your alternative email address"
password = "Google App Password (see README for instructions)"

# this should be the email you want to recieve the images
TO = "your main email"

# the subreddit you want to get images from
subreddit_name = 'animemes'
# the amount of images you want to be sent in a day
image_amount = 10

# the subject of the email the program will send you
subject = 'Daily Dose of r/'
subject += subreddit_name

#_______________________________________END OF USER EDIT VARIABLES_____________________________________

# the sender's email (don't modify)
FROM = email

# initialize email message
msg = MIMEMultipart()
# set the sender's email
msg["From"] = FROM
# set the receiver's email
msg["To"] = TO
# set the subject
msg["Subject"] = subject

# connect to reddit's API
reddit = praw.Reddit(
    client_id="ufRdeda-XoL17T9F7KxKWA",
    client_secret="UJ-K2ExmhW4dvHLh1ps6_Uv3ccEwIQ",
    user_agent="windows:animemesscraper:v1 (by /u/LateVanilla5536)",
)

# loop through the top images from posts on the subreddit. Attempt
# to add each image to the email message until the image_amount has been reached
counter = 1
for submission in reddit.subreddit(subreddit_name).hot(limit=None):
    print(counter)
    print(submission.url)
    if counter > image_amount:
        break
    # handles checks and adding image to the message
    if (not submission.is_self) and (('.jpg' in submission.url) or '.png' in submission.url):
        img_data = requests.get(submission.url).content
        try:
            image = MIMEImage(img_data)
            msg.attach(image)
            counter += 1
        except:
            continue

#send the email
send_mail(email, password, FROM, TO, msg)


# =============================================================================================================
