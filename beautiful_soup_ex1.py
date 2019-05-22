# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:16:22 2019

@author: Jayesh Kumar Tiwari
"""
import requests
from bs4 import BeautifulSoup

#fetch URL of the website to be scrapped
URL = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States#Presidents'
r = requests.get(URL)
print(r.status_code) #it prints the status code (must start with 2(like 200))

#Now we introduce an object 'soup' which stores the content of the requested page
soup = BeautifulSoup(r.content, 'lxml')

#As our table is in the tag table and class wikitable. So, first we will
#abstract data in table tag usin find method of bs4 object
#This method returns a bs4 object
tb = soup.find('table', class_= 'wikitable')

#Now, we are interested only in the names of the presidents. And they are given in
# the 'a' tag of the parent tag 'b'.
# When we run a for loop in the objects of tb.find_all('b')
# We assign name as the names in 'a' tag using find method
# If you will print name, then whole link will get printed.
# so only text will come from get_text('title') 
for link in tb.find_all('b'):
    name = link.find('a')
    print(name.get_text('title'))


