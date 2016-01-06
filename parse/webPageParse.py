'''
Created on Jan 6, 2016

@author: Yamaan

This script is for testing purposes
This will only run in PYTHON 2.7.10!
'''

from bs4 import BeautifulSoup
import urllib2
from lxml import html

url = raw_input("Please input url: ")
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
req = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(req)
htmlString = response.read()
soup = BeautifulSoup(htmlString, 'lxml')
print(soup.title.string)
print(soup.p)
print(soup.a)
print(soup.find_all('content'))