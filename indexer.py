#!/usr/bin/python
################################################################################
#   iRGBit's indexhelper for reading texts and helping with creating an index  #
#   http://www.github.com/iRGBit                                               #
################################################################################

import sys
import string

defaultFile = 'files/sample.txt'
defaultStopWords = 'stop_words.txt'

def main():
    if len(sys.argv) > 3:
        print
        print "Usage: python indexer.py <yourFile> <stopWords>"
        print "If no arguments are given %s and %s will be used as default files" % (defaultFile, defaultStopWords)
        print
        sys.exit()
    elif len(sys.argv) == 3:
        yourStopWords = sys.argv[2]
        yourFile = sys.argv[1]

    elif len(sys.argv) == 2:
        yourStopWords = defaultStopWords
        yourFile = sys.argv[1]

    elif len(sys.argv) == 1:
        yourStopWords = defaultStopWords
        yourFile = defaultFile

    print 'Using %s as file and %s as stop word reference.' % (yourFile, yourStopWords)
    print 
    indexThem(yourFile, yourStopWords)

def indexThem(yourFile, yourStopWords):
    punct = set(string.punctuation)
    bookWords = open(yourFile).read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
    bookWords = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in bookWords]

    stopWords = open(yourStopWords).read().decode("utf-8-sig").encode("utf-8").splitlines()

    # remove stopWords from finalWords
    finalWords = [x for x in bookWords if x not in stopWords]

    # count single occurences of words
    from collections import Counter
    topWords = Counter(finalWords)

    # calculate average frequency of words to compute average frequency in your text
    total = 0
    for w in topWords:
        total += topWords[w]
    frequent = total/(len(topWords))

    # only add words that have more than average frequency
    tops = {k:v for (k,v) in topWords.iteritems() if v >= frequent}

    # sort by word count
    #cfinal = sorted(tops.items(), key=lambda x: x[1], reverse=True)

    #sort Alphabetically
    final = sorted(tops.items(), key=lambda x: x[0])

    for x in range(len(final)):
        print '%s: %s' % (final[x][0], final[x][1])

    #bye!


if __name__ == '__main__':
  main()
