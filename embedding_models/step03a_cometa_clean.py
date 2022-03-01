#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mar 3 2022
@author: sap218
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import spacy
import re
from tqdm import tqdm
import string
import random
import json

with open("/cometa/cometa.json", "r") as f:
    original_fora = json.loads(f.read())

filtered_list_topic_posts = {}
filtered_allposts = []
filtered_allposts_wordcount = []
for fora_topic, fora_topic_posts in original_fora.items():
    filt_posts = []
    for one_post in fora_topic_posts:
        if isinstance(one_post, float):
            print("empty: \t", one_post)
        else:
            filt_posts.append(one_post)
            filtered_allposts.append(one_post)
            one_post = one_post.split(" ")
            filtered_allposts_wordcount.append(len(one_post))
    if len(filt_posts) == 0:    print("empty topic: \t", fora_topic)
    else:   filtered_list_topic_posts[fora_topic] = filt_posts
filtered_allposts = sorted(filtered_allposts)
print("\n")
print("topic count: \t", len(filtered_list_topic_posts))
print("post count: \t", len(filtered_allposts))
print("average word count: \t", ((sum(filtered_allposts_wordcount) / len(filtered_allposts_wordcount))))

# https://github.com/kexinhuang12345/clinicalBERT/blob/master/notebook/pretrain.ipynb
def preprocessing(posts): # using clinicalbert pretrain methods
    y = re.sub("<[^<]+?>", '', posts) # removing HTML
    y = re.sub("[^A-Za-z0-9'-]+", ' ', y) # removing chars except '  & - because one words
    y = y.replace("'",'')
    y = y.replace("-",'')
    #y = re.sub(r'\W+', ' ', y) # removing all chars not words
    y = y.replace('\n',' ') # removing newlines
    y = y.replace('\r',' ') # removing newlines
    y = ' '.join(y.split()) # removing extra whitespace
    y = y.lower() # lowercase post
    return y

cleaned_filtered_allposts = []
for one_post in filtered_allposts:
    cleaned_filtered_allposts.append(preprocessing(one_post))

file=open('mbr_pretrain.txt','w')

for i in tqdm(range(len(cleaned_filtered_allposts))):
    if len(cleaned_filtered_allposts[i]) > 0: # remove the one token posts
        note = cleaned_filtered_allposts[i]
        for sent in note:
            file.write(sent)
        file.write('\n')
file.close()

