#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    word_document, number = line.split('\t', 1)
    word, document = word_document.rsplit(',', 1)
    print("%s\t%s,%s") % (document, word, number)