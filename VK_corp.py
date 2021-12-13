#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import json
import requests
from datetime import datetime
import re
import traceback
import time

owner_list = [89094852, 600332, 286747, 85856325, 25205856, 170140130, 13515656, 20629724, 30666517, 22751485, 14448489, 179664673, 727032, 47256091, 32509740, 172149046, 14000591, 17833376, 4503260, 174859206, 55387604, 27666606, 25336774, 62830729, 48247547, 91453124, 57882883, 1314709]

def parsecorp(owner):
	post_list = []
	try:
		corp = open(str(owner) + "_corp.json", "w", encoding='utf-8')
		corp.write("[")			
		req = requests.get("https://api.vk.com/method/wall.get?owner_id=-" + str(owner) + "&filter=owner&counter=100&offset=1000&v=5.131&access_token=b7e98614b7e98614b7e9861418b793abb9bb7e9b7e98614d672dec5baa80f1b3431c982")
		data = req.json()
		for text in data['response']['items']:
			post_list.append(text["id"])
			time.sleep(1)
			date_text = text['date']
			ts = (date_text)
			ts = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
			text = text['text']
			#print(text)
			#print(ts)
			json.dump({"ts": ts, "text": text}, corp, ensure_ascii=False, indent=4, separators=(',', ': '))
			corp.write(", ")
		#print('owner + 1')
		corp.write("]")
		corp.close()

		corp = open(str(owner) + "_corp.json", "r", encoding='utf-8')
		text_corp = corp.read()
		a = text_corp.replace("}, ]", "}]")

		with open(str(owner) + '_corp.json', 'w') as file:
		  file.write(a)
		corp.close()
		for post_id in post_list:
			parsecomment(owner, post_id)
			time.sleep(1)
	except Exception as e:
		print("wall", e)
		print(data)

def parsecomment(owner, post_id):
	print("owner, post_id", owner, post_id)
	try:			
		req = requests.get("https://api.vk.com/method/wall.getComments?owner_id=-" + str(owner) + "&post_id=" + str(post_id) +"&v=5.131&access_token=b7e98614b7e98614b7e9861418b793abb9bb7e9b7e98614d672dec5baa80f1b3431c982")
		data = req.json()
		print(data['response']['items'])
		if len(data['response']['items']) == 0:
			return
		corp_comments = open(str(owner) + "_" + str(post_id)+"_corp_comments.json", "w", encoding='utf-8')
		corp_comments.write("[")
		for text in data['response']['items']:
			date_text = text['date']
			ts = (date_text)
			ts = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
			text = text['text']
			print(text)
			json.dump({"ts": ts, "text": text}, corp_comments, ensure_ascii=False, indent=4, separators=(',', ': '))
			corp_comments.write(", ")
		print('owner + 1')
		corp_comments.write("]")
		corp_comments.close()

		corp_comments = open(str(owner) + "_" + str(post_id)+ "_corp_comments.json", "r", encoding='utf-8')
		text_corp = corp_comments.read()
		a = text_corp.replace("}, ]", "}]")

		with open(str(owner) + "_" + str(post_id)+'_corp_comments.json', 'w') as file:
		  file.write(a)

		corp_comments.close()
	except Exception as e:
		print("comment",e)
		print(data)

for owner in owner_list:
	parsecorp(owner)



