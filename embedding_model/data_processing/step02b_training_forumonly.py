#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Aug 23 2021
@author: sap218
"""

from time import time  # To time our operations
import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

import gensim
import numpy as np
clinicalbert = gensim.models.KeyedVectors.load('clinicalbert.model') # you may need to edit this depending where you store ClinicalBERT model
weights_clinicalbert_matrix = clinicalbert[clinicalbert.wv.vocab]
weights_clinicalbert_cols = np.shape(clinicalbert[clinicalbert.wv.vocab])[1]
vocab_clinicalbert = list(clinicalbert.wv.vocab)


list_of_posts = []
with open('forum_sentences_pretrain.txt', 'r') as f:
    for l in f.readlines():
        list_of_posts.append(l.replace("\n",""))
cleaned_list_of_posts = list(filter(None, list_of_posts)) # removing empty posts

from nltk.tokenize import word_tokenize
cleaned_list_of_posts_token = []
for post in cleaned_list_of_posts:
    cleaned_list_of_posts_token.append(word_tokenize(post))



# https://www.kaggle.com/pierremegret/gensim-word2vec-tutorial#Training-the-model
# https://radimrehurek.com/gensim/models/word2vec.html
import multiprocessing
cores = multiprocessing.cpu_count()
from gensim.models import Word2Vec

"""
below uses the same parameters as the ClinicalBERT model, you may want to edit this is you don't want to involve ClinicalBERT
"""
model = Word2Vec(min_count = clinicalbert.min_count,
                     window = clinicalbert.window,
                     size = weights_clinicalbert_cols,
                     sample = clinicalbert.sample, 
                     alpha = clinicalbert.alpha, 
                     min_alpha = clinicalbert.min_alpha, 
                     negative = clinicalbert.negative,
                     workers=cores-1,
                     seed=123,
                     max_vocab_size=None)
#t = time()
model.build_vocab(cleaned_list_of_posts_token, progress_per=10000) # building vocabulary
#print('Time to build vocab: {} mins'.format(round((time() - t) / 60, 2)))

model.train(cleaned_list_of_posts_token, total_examples=clinicalbert.corpus_count, epochs=clinicalbert.iter)




model.save('patientforum.model') # save model

weights_patientbert_matrix = model[model.wv.vocab]
weights_patientbert_cols = np.shape(model[model.wv.vocab])[1]
vocab_patientbert = list(model.wv.vocab)
