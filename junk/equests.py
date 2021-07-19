# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:46:01 2021

@author: AVINASH
"""

import requests
import json
import pprint

url = "https://hs-consumer-api.espncricinfo.com/v1/global/fastscore/message/base?messageId=md-1248765-1612272567035"
x = requests.get(url)
x = json.loads(x.text)
pprint.pprint(x)


#getting time in milliseconds

import time
feed = 1612272567000
url = "https://hs-consumer-api.espncricinfo.com/v1/global/fastscore/message/base?messageId=md-1248765-"

c = 1
while c:
    try:
        x = requests.get(url+str(feed))
        x = json.loads(x.text)
        print(" -----------------------------------------------------"+feed)
        feed+=1
    except:
        feed+=1
        continue