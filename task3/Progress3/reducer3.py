#!/usr/bin/env python

from __future__ import division
import sys
import math

def cal_tf(word_number, word_total):
    return word_number/word_total

def cal_idf(total_doc, include_doc):
    num = total_doc/(include_doc + 1)
    return num

current_word = None
current_document_count = 0
word = None

all_document = []
container = {}
doc_count_container = {} # word:current_document_count
for line in sys.stdin:
    line = line.strip()
    word, other_items = line.split('\t', 1)
    items = other_items.split(",")
    document = items[0]
    number = items[1]
    total = items[2]
    count = items[3]
    try:
        number = int(number)
        total = int(total)
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_document_count += count
        
        container[word].append({'document': document, 'tf': cal_tf(number, total)})
    else:
        
        doc_count_container[current_word] = current_document_count
        current_word = word
        current_document_count = count
        
        if word not in container:
            container[word] = list()
        container[word].append({'document': document, 'tf': cal_tf(number, total)})

    if document not in all_document:
        all_document.append(document)

if current_word not in doc_count_container:
    doc_count_container[current_word] = current_document_count
total_document = len(all_document)

for w in container:
    for index, val in enumerate(container[w]):
        tf_idf = val['tf'] * cal_idf(total_document, doc_count_container[w])
        print("%s,%s\t%s") % (w, val['document'], tf_idf)
