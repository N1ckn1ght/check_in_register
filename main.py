import os
import socket
from urllib.parse import urlparse

print('Input URL:')
url = input()
domain = urlparse(url).netloc
try:
    ip = socket.gethostbyname(domain)
except BaseException:
    ip = False

url_found = False
domain_found = False
ip_found = False

inf = open('./register.txt', encoding="utf-8")
for line in inf.readlines():
    s = list(line.strip().split(';'))
    s[1].split(',')
    if (isinstance(s[1], str)):
        if (s[1] == url):
            url_found = True
    elif (isinstance(s[1], list)):
        for i in s[1]:
            if (i == url):
                url_found = True
    s[2].split(',')
    if (isinstance(s[2], str)):
        if (s[2] == domain):
            domain_found = True
    elif (isinstance(s[2], list)):
        for i in s[2]:
            if (i == domain):
                domain_found = True
    s[3].split(',')
    if (isinstance(s[3], str)):
        if (s[3] == ip):
            ip_found = True
    elif (isinstance(s[3], list)):
        for i in s[3]:
            if (i == ip):
                ip_found = True

if (url_found):
    print('URL is in the list.')
else:
    print('URL is not in the list.')
if (domain_found):
    print('Domain', domain, 'is in the list.')
else:
    print('Domain', domain,' is not in the list.')
if (ip):
    if (ip_found):
        print('IP:', ip, 'is in the list.')
    else:
        print('IP:', ip, 'is not in the list.')
else:
    print('IP is unknown.')
