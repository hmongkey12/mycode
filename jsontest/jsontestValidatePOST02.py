#!/usr/bin/python3

import requests
import json


timeURL = "http://time.jsontest.com"
ipURL = "http://ip.jsontest.com/"
validateURL = "http://validate.jsontest.com/"

with open('myservers.txt') as f:
    lines = f.readlines()

timeresp = requests.get(timeURL)
ipresp = requests.get(ipURL)


timejson = timeresp.json()
ipjson = ipresp.json()


query = f"\{'time':{timejson}, 'ip':{ipjson}, 'mysvrs':{lines}\}"
mydata = {"json": query}

validresp = requests.post(validateURL, data=mydata)

print(validresp.json())
