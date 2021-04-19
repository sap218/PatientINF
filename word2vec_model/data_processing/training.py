#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 2021
@author: sap218
"""

import gensim
from nltk.tokenize import word_tokenize

model = gensim.models.KeyedVectors.load('clinicalbert_word2vec.model') # this should be the model you downloaded
weights = (model[model.wv.vocab])
words = list(model.wv.vocab) # summarize vocabulary


list_of_text = []
with open('fora_unformatted.txt', 'r') as f: # 
    for l in f.readlines():
        list_of_text.append(l)
list_of_text_parsing = []
for post in list_of_text:
    post = post.replace("\n"," ").replace("\r"," ").replace("  ", " ").replace("  ", "") # just a final check to make sure \n\r are correct when importing
    if post == " ":
        pass
    else:
        list_of_text_parsing.append(post)

list_of_text_parsing = list(set(list_of_text_parsing)) # set to avoid duplicates
list_of_text_parsing_token = []
for post in list_of_text_parsing:
    list_of_text_parsing_token.append(word_tokenize(post))

model.build_vocab(list_of_text_parsing_token, update=True) 
model.train(list_of_text_parsing_token, total_examples=model.corpus_count, epochs=model.iter)

model.save('../patient-forum_clinicalbert.bin') # save model
