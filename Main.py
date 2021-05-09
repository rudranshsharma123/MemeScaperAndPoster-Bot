import sys
sys.path.append('C:\\Users\\gaura\\Desktop')
# print(sys.path)
from InstaBotPoster import instagramBot
# from FbPoster import fbPoster
from cockroach import cockroachDB
from redditScraper import RedditHandler

import praw
import datetime
import random
import os
import urllib.request as req
import argparse
import pandas as pd
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from instabot import Bot
import PIL
import PIL.Image 
import shutil
import os

import psycopg2


#ENVIORMENT VARIABLES------>
#1----> Reddit <-------
user_agent = 'your user ID'
client_id = 'your cient ID'
client_secret = 'your cleint Secret'
reddit = praw.Reddit(client_id=client_id, client_secret = client_secret,
                        user_agent = user_agent)

redditbot = RedditHandler(reddit)

# 2 ------> Facebook <--------
# option = Options()
# option.add_argument("--disable-infobars")
# option.add_argument("--disable-extensions")
# driver = webdriver.Firefox(executable_path="C:/Users/gaura/Desktop/geckodriver", options=option)
# driver.get("https://www.facebook.com/")
# usernameFaceBook = "facebook.rudransh@gmail.com"
# passwordFaceBook = "rudra1609"

# fb = fbPoster(driver)
# fb.login(id = usernameFaceBook, password=passwordFaceBook)
# fb.go_to_page()

#3 -------> Instagram <-------
# shutil.rmtree("C:/Users/gaura/Desktop/Reddit Proj/config")


#4 CockRoach DB
conn = psycopg2.connect(
    database='your db',
    user='your username',
    password='your password',
    sslmode='require',
    port=26257,
    host='free-tier.gcp-us-central1.cockroachlabs.cloud',
    options="--cluster=your db name"
)
roach = cockroachDB(conn)


#--------> Main Code ->>>>>>>

#Scrping Reddit for posts

a = redditbot.get_posts(10, 'cursedcomments', 'new')
while len(a)<=9:
    pass
b = None
b= redditbot.save_all('cursedcomments')
while not b:
    pass
#getting the posts from reddit
images = redditbot.return_values()
while len(images) <2:
    pass
print(len(images))
#adding Images to CockRoach DB
print(len(images[0]))
# for i in images:
#     fb.post_on_page(i[1])

check = None
check = roach.create_table()
while not check:
    pass
check = None
check = roach.add_values(images)
while not check:
    pass

#Getting Images from CockRoachDB
im = roach.get_values(printing= False)
while not images:
    pass

# Correcting the images values for Instagram (I was planning to host a Google Cloud VM to remove the need for hard coding this step)
directory = "C:/Users/gaura/Desktop/cursedcomments"
imagesForInsta = []
for filename in os.listdir(directory):
    f = directory+'/'+filename
    # checking if it is a file
    if os.path.isfile(f):
        imagesForInsta.append(f)

#posting on instagram
userName = 'your username'
passWord = 'your passwords'
myBot = Bot()
myBot = instagramBot(myBot)
myBot.post_on_page(images = imagesForInsta)

