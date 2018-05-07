#!/usr/bin/python
import requests
import os
import urllib3

urllib3.disable_warnings()

f = open("/tmp/notify-service.txt", "r")
readFile = f.read()
findcritical = readFile.find("CRITICAL")
findrecovery = readFile.find("RECOVERY")

#print(findFile)
os.remove("/tmpnotify-service.txt")

if (findcritical >= 0):

       
        ACCESS_TOKEN = '#'   
        payload = {'message': readFile}
        headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
        r = requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers, verify=False)
        print(r)

elif (findrecovery >= 0):

        
        ACCESS_TOKEN = '#'
        payload = {'message': readFile}
        headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
        r = requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers, verify=False)
        print(r)
else:
       print "Fale"
