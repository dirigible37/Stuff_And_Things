#!/usr/bin/python

import requests
import json
import smtplib
import re

url = 'http://www.reddit.com/r/buildapcsales/new.json'
headers = {'user-agent' : 'awesome deals by /u/dirigible'}

bapc = requests.get(url, headers=headers)
bapc_json = bapc.json()

chance_keywords = ['ITX', 'NCASE'];
winslow_keywords = ['1440'];
johnny_keywords = ['1060'];

def createMessage(title, link, perma):
	message = """
	Hey nerd, I found a deal for you!
	If you were wondering, the post is: """+title+"""
	You can find a link to the deal here: """+link+"""
	The comments are here: http://www.reddit.com/"""+perma+"""
	"""
	return message


for post in bapc_json['data']['children']:
	title =  post['data']['title']
	link = post['data']['url']
	perma = post['data']['permalink']
	message = createMessage(title, link, perma)
	if title not in open('past_deals').read():
		for keyword in chance_keywords:
			if title.upper().find(keyword) != -1:
				print title;
				sender = 'mohw011@gmail.com'
				receivers = ['mohw011@gmail.com', 'sweepthepitch1@gmail.com']
				
				open('past_deals', 'a').write(title+"\n");
				smtpObj = smtplib.SMTP('localhost')
				smtpObj.sendmail(sender, receivers, message)         
		for keyword in winslow_keywords:
			if title.upper().find(keyword) != -1:
				print title;
				sender = 'mohw011@gmail.com'
				receivers = ['mohw011@gmail.com']

				open('past_deals', 'a').write(title+"\n");
				smtpObj = smtplib.SMTP('localhost')
				smtpObj.sendmail(sender, receivers, message)         
		for keyword in johnny_keywords:
			if title.upper().find(keyword) != -1:
				print title;
				sender = 'mohw011@gmail.com'
				receivers = ['mohw011@gmail.com', 'theofficialninja@gmail.com']

				open('past_deals', 'a').write(title+"\n");
				smtpObj = smtplib.SMTP('localhost')
				smtpObj.sendmail(sender, receivers, message)         

url = 'http://www.reddit.com/r/hardwareswap/new.json'
headers = {'user-agent' : 'awesome deals by /u/dirigible'}

hws = requests.get(url, headers=headers)
hws_json = hws.json()

for post in hws_json['data']['children']:
	title =  post['data']['title']
	link = post['data']['url']
	perma = post['data']['permalink']
	message = createMessage(title, link, perma)
	if title not in open('past_deals').read():
		for keyword in chance_keywords:
			if title.upper().find(keyword) != -1:
				print title;
				sender = 'mohw011@gmail.com'
				receivers = ['mohw011@gmail.com', 'sweepthepitch1@gmail.com']

				open('past_deals', 'a').write(title+"\n");
				smtpObj = smtplib.SMTP('localhost')
				smtpObj.sendmail(sender, receivers, message)         
		for keyword in winslow_keywords:
			if title.upper().find(keyword) != -1:
				print title;
				sender = 'mohw011@gmail.com'
				receivers = ['mohw011@gmail.com']

				open('past_deals', 'a').write(title+"\n");
				smtpObj = smtplib.SMTP('localhost')
				smtpObj.sendmail(sender, receivers, message)         
		for keyword in johnny_keywords:
			if title.upper().find(keyword) != -1:
				print title;
				sender = 'mohw011@gmail.com'
				receivers = ['mohw011@gmail.com', 'theofficialninja@gmail.com']

				open('past_deals', 'a').write(title+"\n");
				smtpObj = smtplib.SMTP('localhost')
				smtpObj.sendmail(sender, receivers, message)         
