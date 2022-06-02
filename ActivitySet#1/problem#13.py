# Network Programming
# https://www.py4e.com/lessons/network
'''import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()'''

'''
from urllib import request
from bs4 import BeautifulSoup

html=request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html').read()
soup = BeautifulSoup(html)
tags=soup('span')
sum=0
for tag in tags:
    
    sum=sum+int(tag.contents[0])
print(sum)'''


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
for tag in tags:
    x = re.findall('[0-9]+', str(tags))

sum=0
for i in x:
    sum = sum + int(i)
print(sum