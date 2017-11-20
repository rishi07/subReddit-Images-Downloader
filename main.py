# dependencies
# pip install praw
# pip install wget

import os
import praw
import re
import sys
import requests 
import urllib
import urllib2
from subprocess import call
import wget
import time

reddit = praw.Reddit(client_id = '<insert client id>',
				     client_secret = '<insert client secret>',
				     user_agent = '<insert user agent>',
				     username = '<insert username here>',
				     password = '<insert password here>' 
				     )
# print (reddit.read_only) 
subr = str(raw_input())
pkp =  os.getcwd()

if not os.path.exists(subr):
    os.makedirs(subr)


folderpath = str(pkp) +'/'+ subr +'/'
# print folderpath
os.chdir(folderpath) 

i = 1
pkp = list()
for submission in reddit.subreddit(subr).top(limit=None):

	url2 = submission.url
	if '/i.' in url2:
		f = urllib2.urlopen(url2)
		f2 = str(url2)
		extention = f2.split(".")
		extentionstr = str(extention[-1])
		extentionstr = extentionstr.strip('/\\')
		fname = str(i)+"."+extentionstr	
		print fname
		try:
			with open(fname,"wb") as img:
				img.write(f.read())
		except:
			print "some error encountered :D \n\n"
		print url2
		print i,"^---\n"
		i+=1
		if(i%20==0):
			time.sleep(2)
