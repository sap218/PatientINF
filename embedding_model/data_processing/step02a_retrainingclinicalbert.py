#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Aug 23 2021
@author: sap218
"""

import numpy as np

import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

import gensim
model = gensim.models.KeyedVectors.load('clinicalbert.model') # you may need to edit this depending where you store ClinicalBERT model

weights_org_model_matrix = model[model.wv.vocab]
weights_org_model_cols = np.shape(model[model.wv.vocab])[1]
vocab_org_model = list(model.wv.vocab)


list_of_posts = []
with open('forum_sentences_pretrain.txt', 'r') as f:
    for l in f.readlines():
        list_of_posts.append(l.replace("\n",""))
cleaned_list_of_posts = list(filter(None, list_of_posts)) # removing empty posts

from nltk.tokenize import word_tokenize
cleaned_list_of_posts_token = []
for post in cleaned_list_of_posts:
    cleaned_list_of_posts_token.append(word_tokenize(post))



model.build_vocab(cleaned_list_of_posts_token, update=True,)# max_vocab_size=None)
model.train(cleaned_list_of_posts_token, total_examples=model.corpus_count, epochs=model.iter,)# max_vocab_size=None,)#, seed=123,


model.save('patientforum+clinical.model') # save model


weights_upd_model_matrix = model[model.wv.vocab]
weights_upd_model_cols = np.shape(model[model.wv.vocab])[1]
vocab_upd_model = list(model.wv.vocab)
