#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Aug 23 2021
@author: sap218
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import spacy
import re
from tqdm import tqdm
import string

import json
with open("patient-info_forums.json", "r") as f:
    original_fora = json.loads(f.read())

list_of_all_posts = []
for topic, list_of_threads in original_fora.items():
    for thread in list_of_threads:
        list_of_all_posts.append(thread["title"]) # including 
        list_of_all_posts.append(thread["post"])
        for list_of_replies in thread["replies"]:
            list_of_all_posts.append(list_of_replies["post"])
            for inner_list_of_replies in list_of_replies["replies"]:
                list_of_all_posts.append(inner_list_of_replies["post"])
list_of_all_posts = list(filter(None, list_of_all_posts)) # removing empty posts


# https://github.com/kexinhuang12345/clinicalBERT/blob/master/notebook/pretrain.ipynb
def preprocessing(posts): # using clinicalbert pretrain methods
    y = re.sub('<[^<]+?>', '', posts) # removing HTML
    y = re.sub(r'\W+', ' ', y) # removing all chars not words
    y = y.replace('\n',' ') # removing newlines
    y = y.replace('\r',' ') # removing newlines
    y = ' '.join(y.split()) # removing extra whitespace
    y = y.lower() # lowercase post
    return y
cleaned_list_all_posts = []
for post in list_of_all_posts:
    cleaned_list_all_posts.append(preprocessing(post))


from spacy.lang.en import English
nlp = English()  # just the language with no model
nlp.add_pipe(nlp.create_pipe('sentencizer'))
def toSentence(x):
    doc = nlp(x)
    text=[]
    try:
        for sent in doc.sents:
            st=str(sent).strip() 
            if len(st)<20:
                #a lot of abbreviation is segmented as one line. But these are all describing the previous things
                #so I attached it to the sentence before
                if len(text)!=0:
                    text[-1]=' '.join((text[-1],st))
                else:
                    text=[st]
            else:
                text.append((st))
    except:
        print(doc)
    return text

pretrain_sent = []
for post in cleaned_list_all_posts:
    pretrain_sent.append(toSentence(post))


file=open('forum_sentences_pretrain.txt','w')
#pretrain_sent = pretrain_sent.values
for i in tqdm(range(len(pretrain_sent))):
    if len(pretrain_sent[i]) > 0: # remove the one token posts
        note = pretrain_sent[i]
        for sent in note:
            file.write(sent)
        file.write('\n')
file.close()
