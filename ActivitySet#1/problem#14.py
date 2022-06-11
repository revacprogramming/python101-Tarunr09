# Using Web Services
# https://www.py4e.com/lessons/servces

'''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input ('Enter url: ')
print('Retrieving', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall ('comments/comment')

for item in lst:
    count = count + 1
    t = item.find ('count').text
    total = total + float (t)
    
print ('Count:', count)
print ('Sum:' , total)'''

import urllib.request, urllib.parse, urllib.error
import json

url = input ('Enter url: ')
print('Retrieving', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('User count:', len(info))

for item in info["comments"]:
    number = int(item["count"])
    count = count + number
print(count