#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mar 3 2022
@author: sap218
"""

from time import time  # To time our operations
import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

import gensim
import numpy as np
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


cleaned_list_of_posts_token = []
for post in cleaned_list_of_posts:
    cleaned_list_of_posts_token.append(post.split(" "))



# https://www.kaggle.com/pierremegret/gensim-word2vec-tutorial#Training-the-model
# https://radimrehurek.com/gensim/models/word2vec.html
import multiprocessing
cores = multiprocessing.cpu_count()
from gensim.models import Word2Vec

model = FastText(min_count = clinicalbert.min_count,
                     window = clinicalbert.window,
                     size = weights_clinicalbert_cols,
                     sample = clinicalbert.sample, 
                     alpha = clinicalbert.alpha, 
                     min_alpha = clinicalbert.min_alpha, 
                     negative = clinicalbert.negative,
                     workers=cores-1,
                     seed=12345,
                     max_vocab_size=None)
model.build_vocab(cleaned_list_of_posts_token, progress_per=10000) # building vocabulary
model.train(cleaned_list_of_posts_token, total_examples=clinicalbert.corpus_count, epochs=clinicalbert.iter)

if experiment == "original": model.save('pi.model') # save model
else: model.save('pi_validation.model') # save model


