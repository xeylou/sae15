import requests
import os 
import urllib
import json

f = open("lg.txt", "r")
listip=[]
for ligne in f :
    a=ligne.split(" ")
    listip.append(a[0])
print(listip)

while True:
    ip=input("Quelle est l'ip cible: ")
    url="http://ip-api.com/json/"
    response=urllib.request.urlopen(url+ip)
    data=response.read()
    values=json.loads(data)

    print(" IP: " + values['query'])
    print(" City: " + values['city'])
    print(" ISP: " + values['isp'])
    print("Country: " + values['country'])
    print("Region: " + values['region'])
    print("Time zone: " + values['timezone'])
    print("Latitude: " , values['lat'])
    print("Longitude: " , values['lon'])

    break