#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:36:23 2020

@author: samantha
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

discussions = pd.read_csv('test_topics.tsv', sep='\t')

topics = list(discussions['inflammation'])
urls = list(discussions['patient.info link'])



final_map = {}

final_map_keys = {}


for url in urls:
    #url = 'https://patient.info/forums/discuss/browse/cellulitis-391'
    #url = 'https://patient.info/forums/discuss/browse/arthritis-241'
    
    
    response = requests.get(url) # requesting
    soup = BeautifulSoup(response.text, 'html.parser') # souping
    
    
    
    page_count = soup.findAll('option', attrs={'selected': 'selected'})
    counts = []
    for p in page_count:
        p = p.text.strip() # strip() to remove starting and trailing
        counts.append(p)    
        
    page_count = []
    for word in counts[0].split('/'):
       if word.isdigit():
          page_count.append(int(word))
    page_count = page_count[1]
    
    
    
    

    threads_list = []
    
    for x in range(page_count):
        payload = {'page':x}
        response = requests.get(url, params=payload)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        
        thread = soup.findAll('h3', attrs={'class': 'post__title'})
        
        threads = {}
        
        for t in thread:
            
            link = t.findAll('a', attrs={'rel': 'discussion'})
            for l in link:
                u = "https://patient.info%s" % (l['href'])
                
            t = t.text.strip() 
            
            try:
                threads[u] = t
            except:
                pass
            
            
            
        for t in thread:
            link = t.findAll('a', attrs={'rel': 'nofollow'})
            for l in link:
                u = "https://patient.info%s" % (l['href'])
                
            t = t.text.strip() 
            
            try:
                threads[u] = t
            except:
                pass          
            
            
            
        
        threads_list.append(threads)
        
        
        
    
    list_of_topics = {}
    for d in threads_list:
        list_of_topics.update(d)


    final_map[url] = list_of_topics

    final_map_keys[url] = list(list_of_topics.keys())


with open('topics_links.json', 'w') as fp:
    json.dump(final_map_keys, fp, indent=4)
    