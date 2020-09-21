#!/usr/bin/env python3


import requests

#print(dir(requests))

response=requests.get('https://github.com/thakurmhn/')

#print(dir(response))

if response.status_code == 200:
    print("Response is Good")
else:
    print("Site is not reachable")


#print(response.headers)
#print(response.text)
