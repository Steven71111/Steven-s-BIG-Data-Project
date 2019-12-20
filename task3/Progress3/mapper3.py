#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    word_document, number_total = line.split('\t', 1)
    word, document = word_document.rsplit(',', 1)
    number, total = number_total.rsplit(',', 1)
    print("%s\t%s,%s,%s,%s") % (word, document, number, total, 1)
