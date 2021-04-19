#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 2021
@author: samantha
"""

import json
import re

html_re = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});') # https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string


with open('patient-info_forums.json') as f:
    original_json = json.load(f)

list_of_texts = []
for url,list_of_threads in original_json.items():
    for thread in list_of_threads:
        post = (thread["title"] + ". " + thread["post"])
        post = html_re.sub("", post).strip().lower()
        post = re.sub("[^A-Za-z0-9.,]+", " ", post)
        post = ''.join([i for i in post if not i.isdigit()])
        post = post.replace(",",", ").replace(" ,",", ").replace(".",". ").replace(" .",". ").replace("..",".").replace(".","").replace(",","")
        post = post.replace("\n",". ").replace("\r",". ").replace("  "," ").replace("  "," ")
        list_of_texts.append(post)

        try:
            for replies in thread["replies"]:
                post = html_re.sub("", replies["post"]).strip().lower()
                post = re.sub("[^A-Za-z0-9.,]+", " ", post)
                post = ''.join([i for i in post if not i.isdigit()])
                post = post.replace(",",", ").replace(" ,",", ").replace(".",". ").replace(" .",". ").replace("..",".").replace(".","").replace(",","")
                post = post.replace("\n",". ").replace("\r",". ").replace("  "," ").replace("  "," ")
                list_of_texts.append(post)
                
            try:    
                for inner_replies in replies["replies"]:
                    post = html_re.sub("", inner_replies["post"]).strip().lower()
                    post = re.sub("[^A-Za-z0-9.,]+", " ", post)
                    post = ''.join([i for i in post if not i.isdigit()])
                    post = post.replace(",",", ").replace(" ,",", ").replace(".",". ").replace(" .",". ").replace("..",".").replace(".","").replace(",","")
                    post = post.replace("\n",". ").replace("\r",". ").replace("  "," ").replace("  "," ")
                    list_of_texts.append(post)
            except:
                print(inner_replies["post"])
                
        except:
            print(replies["post"])
                      
list_of_texts_set = list(set(list_of_texts))
del list_of_texts_set[0]
del list_of_texts_set[39964]

list_of_texts_set_together = "\n".join(list_of_texts_set)
list_of_texts_set_together = list_of_texts_set_together.replace("\n ", "\n")

with open("fora_unformatted.txt", "w") as text_file:
    text_file.write(list_of_texts_set_together)
