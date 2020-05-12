#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:52:41 2020

@author: samantha
"""


import requests
from bs4 import BeautifulSoup



#url = 'https://patient.info/forums/discuss/too-much-joint-pain-any-good-home-remedies-for-relief--684622'
url = 'https://patient.info/forums/discuss/arthritis-of-the-fingers-735848'



response = requests.get(url) # requesting
soup = BeautifulSoup(response.text, 'html.parser') # souping


reply_count = soup.find('h2', attrs={'class': 'reply__title u-h4'})
reply_count = reply_count.text.strip() # strip() to remove starting and trailing
replies = []
for word in reply_count.split():
   if word.isdigit():
      replies.append(int(word))

page_count = round(replies[0]/10)
#page_count = page_count - 1







topic = soup.find('article', attrs={'class': 'post mb-0'})

thread = {}
for info in topic: 
    thread_title = soup.find('h1', attrs={'class': 'u-h1 post__title'}) 
    thread_title = thread_title.text.strip() 
    thread['title'] = thread_title
    
    user = soup.find('h5', attrs={'class': 'author__info'})
    user = user.text.strip() 
    thread['user'] = user
    
    thread_topic = soup.find('div', attrs={'class': 'post__content'})
    for content in thread_topic:
        content = soup.find('input', attrs={'class':'moderation-conent'})
        content = content['value']
    thread['post'] = content
    
    date_posted = soup.find('time', attrs={'class': 'fuzzy'})
    date_posted = date_posted['datetime']
    thread['date posted'] = date_posted
    




replies_list = []

for x in range(page_count):
    payload = {'order': 'oldest', 'page': x}
    response = requests.get(url, params=payload)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    article_class = soup.findAll('article', attrs={'class':'post post__root'})
    
    
    post_header_info = [] # replies contents
    
    for article in article_class:
        info = {}
        
        post_header = article.find('div', attrs={'class':'post__header'})
    
        user = post_header.find('a', attrs={'class': 'author__name', 'itemprop':'name'}) # username
        user = user.text.strip() 
        #print(user)
        info['user'] = user
        date_posted = post_header.find('time', attrs={'class': 'fuzzy'}) # date
        date_posted = date_posted['datetime']
        info['date posted'] = date_posted
        #print(date_posted)
      
        
        post_content = article.find('div', attrs={'class':'post__content break-word'}) # comment
        post = post_content.find('p')
        post = post.text.strip() 
        info['post'] = post
            
        post_header_info.append(info)
    
    replies_list.append(post_header_info)
    






replies = [item for sublist in replies_list for item in sublist]





'''
payload = {'order': 'oldest', 'page': 0}
response = requests.get(url, params=payload)

soup = BeautifulSoup(response.text, 'html.parser')
   

article_class = soup.findAll('article', attrs={'class':'post post__root'})


post_header_info = [] # replies contents

for article in article_class:
    info = {}
    
    post_header = article.find('div', attrs={'class':'post__header'})

    user = post_header.find('a', attrs={'class': 'author__name', 'itemprop':'name'}) # username
    user = user.text.strip() 
    #print(user)
    info['user'] = user
    date_posted = post_header.find('time', attrs={'class': 'fuzzy'}) # date
    date_posted = date_posted['datetime']
    info['date posted'] = date_posted
    #print(date_posted)
  
    
    post_content = article.find('div', attrs={'class':'post__content break-word'}) # comment
    post = post_content.find('p')
    post = post.text.strip() 
    info['post'] = post
        
    post_header_info.append(info)
'''