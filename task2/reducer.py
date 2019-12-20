#!/usr/bin/env python

import sys
import json

current_word = None
current_file = dict()
word = None
for line in sys.stdin:
    line = line.strip()
    word, fileCount = line.split('\t', 1)
    file, lineCount = fileCount.rsplit(',', 1)
    try:
        lineCount = int(lineCount)
    except ValueError:
        continue
    if current_word == word:
        if file in current_file:
            current_file[file].append(lineCount)
            current_file[file] = list(set(current_file[file]))
        else:
            current_file[file] = [lineCount]
    else:
        if current_word:
            print ("%s\t%s") % (current_word, json.dumps(current_file))
        current_file[file] = [lineCount]
        current_word = word
if word == current_word:
    print ("%s\t%s") % (current_word, json.dumps(current_file))