#!/usr/bin/env python
import sys
 
# maps words to their counts
final_1 = dict()

w = set()
# input comes from STDIN
for line1 in sys.stdin:
	# remove leading and trailing whitespace
	line1 = line1.strip()
	if('\t'in line1):
		# parse the input we got from mapper.py
		word_fina_1,key = line1.split('\t')
		# convert count (currently a string) to int
		key1 = key.split(',')
		if word_fina_1 not in w:
			w.add(word_fina_1)
	                final_1[word_fina_1] = dict()
		for k in key1:
			if(k not in final_1[word_fina_1]):
				final_1[word_fina_1][k] = 1
			else:
				final_1[word_fina_1][k] = final_1[word_fina_1][k] + 1   
# write the tuples to stdout
# Note: they are unsorted
#print len(w)
for word_fina_1 in final_1:
        print word_fina_1+'\t'+str(final_1[final_1])
