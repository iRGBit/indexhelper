#!/usr/bin/python

import string


punct = set(string.punctuation)
bookWords = open('files/romeo-and-juliet.txt').read().lower().split()
bookWords = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in bookWords]

print bookWords
