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

#setseeds = 1
setseeds = 123 ## THIS ONE ORIGINAL!!!!!!!
#setseeds = 808
#setseeds = 6298948
#setseeds = 2014428590885440

random.seed(setseeds)

with open("patients-info_forums.json", "r") as f:
    original_fora = json.loads(f.read())

word_limit = 1 # was 100 for ClinicalBERT for sampling size

list_of_all_topic_posts = {}
list_of_all_topic_posts_original = {}

list_of_all_topic_posts_original_sums = []

for topic, list_of_threads in original_fora.items():
    list_of_all_posts = []
    list_of_all_posts_original = []
    
    for thread in list_of_threads:
        
        post = thread["title"]
        post_split = post.split(" ")
        if len(post_split) < word_limit: list_of_all_posts_original.append(post)
        else:
            list_of_all_posts.append(post) 
            list_of_all_posts_original.append(post)
            
        post = thread["post"]
        post_split = post.split(" ")
        if len(post_split) < word_limit: list_of_all_posts_original.append(post)
        else:
            list_of_all_posts.append(post) 
            list_of_all_posts_original.append(post)
        
        for list_of_replies in thread["replies"]:
            post = list_of_replies["post"]
            try:
                post_split = post.split(" ")
                if len(post_split) < word_limit: list_of_all_posts_original.append(post)
                else:
                    list_of_all_posts.append(post) 
                    list_of_all_posts_original.append(post)
            except:
                pass
            
            for inner_list_of_replies in list_of_replies["replies"]:
                post = inner_list_of_replies["post"]
                try:
                    post_split = post.split(" ")
                    if len(post_split) < word_limit: list_of_all_posts_original.append(post)
                    else:
                        list_of_all_posts.append(post) 
                        list_of_all_posts_original.append(post)
                except:
                    pass
                
    list_of_all_posts = list(filter(None, list_of_all_posts)) # removing empty posts
    list_of_all_posts_original = list(filter(None, list_of_all_posts_original))
    
    list_of_all_topic_posts_original_sums.append(len(list_of_all_posts_original))
    
    list_of_all_topic_posts[topic] = list_of_all_posts
    list_of_all_topic_posts_original[topic] = list_of_all_posts_original



#### POST COUNT AND WORD COUNT ETC
list_of_all_topic_posts_set = {}
for topic, list_of_all_posts in list_of_all_topic_posts_original.items():
    list_of_all_posts = list(set(list_of_all_posts))
    list_of_all_posts.sort()
    list_of_all_topic_posts_set[topic] = list_of_all_posts
list_of_all_posts_flat = []
for topic, list_of_all_posts in list_of_all_topic_posts_set.items():
    for post in list_of_all_posts:
        list_of_all_posts_flat.append(post)
average_word_sizes = []
for post in list_of_all_posts_flat:
    post = post.split(" ")
    average_word_sizes.append(len(post))
print(sum(list_of_all_topic_posts_original_sums), (sum(average_word_sizes) / len(average_word_sizes)))
####




list_of_all_topic_posts_set = {}
for topic, list_of_all_posts in list_of_all_topic_posts.items():
    list_of_all_posts = list(set(list_of_all_posts))
    list_of_all_posts.sort()
    list_of_all_topic_posts_set[topic] = list_of_all_posts
list_of_all_posts_flat = []
for topic, list_of_all_posts in list_of_all_topic_posts_set.items():
    for post in list_of_all_posts:
        list_of_all_posts_flat.append(post)


bioredditcut = 20014 # number of social media posts
clinicalbertcut = 100000 # number of clinical letters

cut_off = int(bioredditcut / len(original_fora)) 

list_of_all_topic_posts_set_cut = {}
for topic, list_of_all_posts in list_of_all_topic_posts_set.items():
    random.Random(setseeds).shuffle(list_of_all_posts)
    #random.shuffle(list_of_all_posts)
    if len(list_of_all_posts) < cut_off:
        list_of_all_posts_cut = list_of_all_posts
        list_of_all_topic_posts_set_cut[topic] = list_of_all_posts_cut
    else:
        list_of_all_posts_cut = list_of_all_posts[:cut_off] # 100000 / 1369
        list_of_all_topic_posts_set_cut[topic] = list_of_all_posts_cut


list_of_all_posts_flat = []
for topic, list_of_all_posts in list_of_all_topic_posts_set_cut.items():
    for post in list_of_all_posts:
        list_of_all_posts_flat.append(post)



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
cleaned_list_all_posts = []
for post in list_of_all_posts_flat:
    cleaned_list_all_posts.append(preprocessing(post))



average_word_sizes = []
for post in cleaned_list_all_posts:
    post = post.split(" ")
    average_word_sizes.append(len(post))
print((sum(average_word_sizes) / len(average_word_sizes)))




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
                #a lot of abbreviation is segmented as one line - but these are all describing the previous things
                #so attached to the sentence before
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







if setseeds == 123:
    file=open('pi_pretrain.txt','w')
    print("EXPERIMENT %s" % setseeds)
else:
    print("VALIDATION EXPERIMENT %s" % setseeds)
    file=open('pi_pretrain_validation.txt','w')


#pretrain_sent = pretrain_sent.values
for i in tqdm(range(len(pretrain_sent))):
    if len(pretrain_sent[i]) > 0: # remove the one token posts
        note = pretrain_sent[i]
        for sent in note:
            file.write(sent)
        file.write('\n')
file.close()


