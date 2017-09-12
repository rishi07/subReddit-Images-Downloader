import os
import praw
import re
import sys
import requests 
import urllib
from subprocess import call
import wget
from time import sleep
import pycurl


reddit = praw.Reddit(client_id = '<insert client id>',
				     client_secret = '<insert client secret>',
				     user_agent = '<insert user agent>',
				     username = '<insert username here>',
				     password = '<insert password here>' 
				     )

print ("Enter name of subreddit ")
subr = input()
pkp =  os.getcwd()


if not os.path.exists(subr):
    os.makedirs(subr)


folderpath = str(pkp) +'/'+ subr +'/'
os.chdir(folderpath) 



i = 1
for submission in reddit.subreddit(subr).hot(limit=None):
	url = submission.url
	if '/i.' in url:
		# result = urllib.urlretrieve(url,'/media/user/X/')
		filename = wget.download(url)
		print("\n saved ",i)
		print ("\n")
		i+=1

		
		
