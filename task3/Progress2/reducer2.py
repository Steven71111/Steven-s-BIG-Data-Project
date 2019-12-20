#!/usr/bin/env python

import sys

current_document = None
current_total_count = 0
document = None

container = {}
for line in sys.stdin:
    line = line.strip()
    document, word_number = line.split('\t', 1)
    word, number = word_number.rsplit(',', 1)
    try:
        number = int(number)
    except ValueError:
        continue

    if current_document == document:
        current_total_count += number
        key = word+","+document
        container[key] = number
    else:
        if len(container) > 0 :
            for k, v in container.items():
                print("%s\t%s,%s") % (k, v, current_total_count)
        current_total_count = number
        current_document = document
        container = {word+","+document : number}

if document == current_document:
    for k, v in container.items():
        print("%s\t%s,%s") % (k, v, current_total_count)