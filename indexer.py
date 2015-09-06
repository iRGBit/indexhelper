#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#   iRGBit's indexhelper for reading texts and helping with creating an index  #
#   http://www.github.com/iRGBit                                               #
#   hypertext ät birgitbachler dot com                                         #
################################################################################

import sys
import string
import numpy

languages = ['EN', 'DE']
mylang = 0;

defaultFile = 'files/sample.txt'
defaultStopWords = 'stopwords/stop_words_%s.txt' % languages[mylang]
defaultOut = 'out.txt'

def main():
    mystring = "Select Language from the following:%s - default is EN: " % (concat(languages))
    slang = raw_input(mystring).upper()
    if slang in languages:
        si = languages[languages.index(slang)]
        yourStopWords = 'stopwords/stop_words_%s.txt' % si
        print "Parsing your text with the %s stopwords" % si
    else:
        yourStopWords = defaultStopWords
        print "Not a valid language. Assuming English..."

    mystring = "Select name of ouput text file (default is %s ): " % defaultOut
    sout = raw_input(mystring)
    if sout=="":
        yourOut = defaultOut
    elif sout.endswith('.txt'):
        yourOut = sout
    else:
        yourOut = sout + '.txt'

    print "Printing your results to %s." % yourOut

    if len(sys.argv) > 2:
        print
        print "Usage: python indexer.py <yourFile>"
        print "If no arguments are given %s and %s will be used as default files" % (defaultFile, defaultStopWords)
        print
        sys.exit()

    elif len(sys.argv) == 2:
        yourFile = sys.argv[1]

    elif len(sys.argv) == 1:
        yourFile = defaultFile
    print 'Using %s as file and %s as stop word reference, printing to %s.' % (yourFile, yourStopWords, yourOut)
    print
    indexThem(yourFile, yourStopWords, yourOut)

def concat(alist):
    outputstring = ""
    for a in alist:
        outputstring = outputstring + " " + a
    return outputstring


def indexThem(yourFile, yourStopWords, yourOut):
    punct = set(string.punctuation)
    bookWords = open(yourFile).read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
    bookWords = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in bookWords]

    stopWords = open(yourStopWords).read().decode("utf-8-sig").encode("utf-8").splitlines()

    # remove stopWords from finalWords
    finalWords = [x for x in bookWords if x not in stopWords]

    # count single occurences of words
    from collections import Counter
    topWords = Counter(finalWords)
    #print topWords

    # following commented out lines of code are for managin the threshold of indexed word within given percentile
    frequence = []
    #pval = 51
    for w in topWords:
        frequence.append(topWords[w])
    #a = numpy.array(frequence)
    #p = numpy.percentile(a, pval)

    # calculate average frequency of words to compute average frequency in your text
    total = 0
    for w in topWords:
        total += topWords[w]

    #print '%s is the total and %s is the length' % (total, len(topWords))
    frequent = total/(len(topWords))

    #print
    #print '%s is a percentile of %s and %s is the average' % (p, pval, frequent)




    # only add words that have more than average frequency
    tops = {k:v for (k,v) in topWords.iteritems() if v >= frequent}

    # sort by word count
    #final = sorted(tops.items(), key=lambda x: x[1], reverse=True)

    #sort Alphabetically
    final = sorted(tops.items(), key=lambda x: x[0])

    outFile=open(yourOut, 'w+')
    for x in range(len(final)):
        print >> outFile, '%s: %s' % (final[x][0], final[x][1])
    outFile.close()

    #bye!


if __name__ == '__main__':
  main()
