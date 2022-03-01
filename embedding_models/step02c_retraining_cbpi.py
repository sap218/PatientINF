#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mar 3 2022
@author: sap218
"""

import numpy as np

import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

from gensim.models.fasttext import FastText # https://radimrehurek.com/gensim/auto_examples/tutorials/run_fasttext.html#saving-loading-models
clinicalbert = FastText.load('../clinicalbert/FastText/fasttext.model')

weights_clinicalbert_matrix = clinicalbert[clinicalbert.wv.vocab]
weights_clinicalbert_cols = np.shape(clinicalbert[clinicalbert.wv.vocab])[1]
vocab_clinicalbert = list(clinicalbert.wv.vocab)


experiment = "original"
#experiment = "validation"

list_of_posts = []

if experiment == "original":
    with open('pi_pretrain.txt', 'r') as f:
        for l in f.readlines():
            list_of_posts.append(l.replace("\n",""))
    cleaned_list_of_posts = list(filter(None, list_of_posts)) # removing empty posts
else:
    with open('pi_pretrain_validation.txt', 'r') as f:
        for l in f.readlines():
            list_of_posts.append(l.replace("\n",""))
    cleaned_list_of_posts = list(filter(None, list_of_posts)) # removing empty posts

from nltk.tokenize import word_tokenize
cleaned_list_of_posts_token = []
for post in cleaned_list_of_posts:
    cleaned_list_of_posts_token.append(word_tokenize(post))

clinicalbert.build_vocab(cleaned_list_of_posts_token, update=True)# max_vocab_size=None)
clinicalbert.train(cleaned_list_of_posts_token, total_examples=clinicalbert.corpus_count, epochs=clinicalbert.iter)# max_vocab_size=None,)#, seed=123,

if experiment == "original": clinicalbert.save('cbpi.model') # save model
else: clinicalbert.save('cbpi_validation.model')

# https://gist.github.com/AbhishekAshokDubey/054af6f92d67d5ef8300fac58f59fcc9

