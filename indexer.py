#!/usr/bin/python

yourFile = 'files/sample.txt'
yourStopWords = 'stop-words_english_1_en.txt'

import string

punct = set(string.punctuation)
bookWords = open(yourFile).read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
bookWords = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in bookWords]

stopWords = open(yourStopWords).read().decode("utf-8-sig").encode("utf-8").splitlines()

finalWords = [x for x in bookWords if x not in stopWords]

from collections import Counter
topWords = Counter(finalWords)

total = 0

for w in topWords:
    total += topWords[w]

frequent = total/(len(topWords))

tops = {k:v for (k,v) in topWords.iteritems() if v > frequent}

# sort by word count
#final = sorted(tops.items(), key=lambda x: x[1], reverse=True)

#sort Alphabetically
final = sorted(tops.items(), key=lambda x: x[0])

for x in range(len(final)):
    print '%s: %s' % (final[x][0], final[x][1])
