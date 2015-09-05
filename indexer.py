#!/usr/bin/python

import string

punct = set(string.punctuation)
bookWords = open('files/huckleberry-finn.txt').read().lower().split()
bookWords = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in bookWords]

#print bookWords

stopWords = open('stop-words_english_1_en.txt').read().decode("utf-8-sig").encode("utf-8").splitlines()
#print stopWords

#from nltk.corpus import stopwords

#stopWords = set(stopwords.words('english'))
#bookWords = nltk.word_tokenize(open('files/huckleberry-finn.txt').read())

#[x for x in bookWords if x not in stopWords]
finalWords = [x for x in bookWords if x not in stopWords]

#print bookWords


from collections import Counter
topWords = Counter(finalWords)
#print topWords
