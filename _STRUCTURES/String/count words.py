"""!"""
"""Программа подсчитывающая количество появления каждого символа"""

import string
import sys
words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
filename = 'file1.txt'
for line in open(filename, encoding="utf-8"):
    for word in line.lower().split():
        word = word.strip(strip)
        if len(word) > 2:
            words[word] = words.get(word, 0) + 1
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))