#!/usr/bin/python

import string

punct = set(string.punctuation)
bookWords = open('files/sample.txt').read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
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

total = 0

for w in topWords:
    total += topWords[w]

frequent = total/(len(topWords))

tops = {k:v for (k,v) in topWords.iteritems() if v > frequent}

final = sorted(tops.items(), key=lambda x: x[1], reverse=True)

for x in range(len(final)):
    print '%s: %s' % (final[x][0], final[x][1])
