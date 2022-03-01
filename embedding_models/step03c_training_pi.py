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

print("\n\n LOADING IN CB MODEL \n\n")

from gensim.models.fasttext import FastText # https://radimrehurek.com/gensim/auto_examples/tutorials/run_fasttext.html#saving-loading-models
clinicalbert = FastText.load('/clinicalbert/FastText/fasttext.model')

weights_clinicalbert_matrix = clinicalbert[clinicalbert.wv.vocab]
weights_clinicalbert_cols = np.shape(clinicalbert[clinicalbert.wv.vocab])[1]
vocab_clinicalbert = list(clinicalbert.wv.vocab)

org_min_count = clinicalbert.min_count
org_window = clinicalbert.window
org_size = weights_clinicalbert_cols
org_sample = clinicalbert.sample
org_alpha = clinicalbert.alpha
org_min_alpha = clinicalbert.min_alpha
org_negative = clinicalbert.negative

org_total_examples=clinicalbert.corpus_count
org_epochs=clinicalbert.iter



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


print("\n\n LOADED \n\n")


cleaned_list_of_posts_token = []
for post in cleaned_list_of_posts:
    cleaned_list_of_posts_token.append(post.split(" "))


print("\n\n JUST QUICKLY TOKENISED \n\n")


# https://www.kaggle.com/pierremegret/gensim-word2vec-tutorial#Training-the-model
# https://radimrehurek.com/gensim/models/word2vec.html
import multiprocessing
cores = multiprocessing.cpu_count()
from gensim.models import Word2Vec


print("\n\n SETTING UP MODEL \n\n")

from gensim.models.fasttext import FastText   # below look at org_ or cb_
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
model = FastText(min_count = org_min_count,
                     window = org_window,
                     size = org_size,
                     sample = org_sample, 
                     alpha = org_alpha, 
                     min_alpha = org_min_alpha, 
                     negative = org_negative,
                     workers=cores-1,
                     seed=12345,
                     max_vocab_size=None)#10000)#780000)None
print("\n\n DONE \n\n")




print("\n\n BUILDING VOCAB \n\n")

model.build_vocab(cleaned_list_of_posts_token, progress_per=1000) # building vocabulary

print("\n\n BUILDED \n\n")
print("\n\n TRAINING \n\n")


model.train(cleaned_list_of_posts_token, total_examples=org_total_examples, epochs=org_epochs)

print("\n\n TRAINED \n\n")
print("\n\n SAVING \n\n")

if experiment == "original": model.save('pi.model') # save model
else: model.save('pi_validation.model') # save model

print("\n\n SAVED \n\n")


