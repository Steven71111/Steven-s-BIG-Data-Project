#!/usr/bin/env python

import sys
import re
import os

file_path = os.environ.get('mapreduce_map_input_file')
file_name = os.path.split(file_path)[-1]

def remove(text):
    remove_chars = '[,:()?\-\-;"".!\'_\[\]]'
    return re.sub(remove_chars, '', text)

countLine = 1
for line in sys.stdin:
    line = remove(line.strip())
    words = line.split()
    for word in words:
        print("%s\t%s,%s") % (word, file_name, countLine)
    countLine += 1