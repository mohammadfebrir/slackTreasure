#!/usr/bin/env python3
#python3
#@author ebi

from pprint import pprint
import json 
import requests
import urllib
import time

# Get channels from your personal/organization's slack
def listChannel(params):
	resp = requests.get("https://slack.com/api/search.messages", params=params)
	return json.loads(resp.text)

def ParsingResponse():
	# Get informations from the slack's pages as much as possible
	page = 1
	loop = True
	while loop is True:
		try :
			params = (
				# Put slack's token here
				('token', ''),

				# Query is keyword you want to look for. In this sample I would like to look for everything related password
				('query', 'password'),
				
				('count', '100'),
				('pretty', '1'),
				('page', page)
			)
			response = listChannel(params)
			totalPage = response['messages']['paging']['pages']
			isPage = response['messages']['paging']['page']
			isPaging = response['messages']['paging']

			page = page + 1
			# stop loop 
			if (totalPage == isPage): 
				loop = False

			# print (response)
			parsingText(response)

		except ValueError:
			print ("[!] Error when get data from slack")

def parsingText(response):
	matches = response['messages']['matches']
	for data in matches:
		from time import sleep
		try:
			print("[+] Channel: {}".format(data.get('channel').get("name")))
			print("[+] User: {}".format(data.get('username')))
			print("[+] Message: {}".format(data.get('text')))
					
			message = "[+] Channel: {}".format(data.get('channel').get("name"))
			message += "[+] User: {}".format(data.get('username'))
			message += "[+] Message: {}".format(data.get('text'))

		except:
			pass

# def sendToSlack(message):
# 	webhook_url = ''
# 	post_data = {
# 		'text': message,
# 	    'channel' : "",
# 	    'username' : ""
# 	}

# 	response = requests.post(
# 		webhook_url, data=json.dumps(post_data),
# 		headers={'Content-Type': 'application/json'}
# 	)

# 	if response.status_code != 200:
# 		raise ValueError(
# 			'Request to slack returned an error %s, the response is:\n%s'
# 			% (response.status_code, response.text)
# 		)

# def sendToEmail(message):
# 	import smtplib, ssl

# 	port = 465  # For SSL
# 	smtp_server = "smtp.gmail.com"
# 	sender_email = ""  # Enter your address
# 	receiver_email = ""  # Enter receiver address
# 	password = "" # Enter your password
# 	message = """ Subject: Test Get Information from Slack"""
# 	context = ssl.create_default_context()
# 	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
# 		server.login(sender_email, password)
# 		server.sendmail(sender_email, receiver_email, message)

def main():
	ParsingResponse()
	print ("Done")

if __name__ == '__main__':
	main()
