#!/usr/bin/env python

import sys

current_word = None
current_document = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word_document, count = line.split('\t', 1)
    word, document_name = word_document.rsplit(',', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        if current_document == document_name:
            current_count += count
        else:
            if current_document:
                print("%s,%s\t%s") % (current_word, current_document, current_count)
            current_count = count
            current_document = document_name
    else:
        if current_word:
            print("%s,%s\t%s") % (current_word, current_document, current_count)
        current_count = count
        current_document = document_name
        current_word = word

if word == current_word:
    print("%s,%s\t%s") % (current_word, current_document, current_count)

