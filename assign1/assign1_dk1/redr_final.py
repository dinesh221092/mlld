#!/usr/bin/env python
import sys
 
# maps words to their counts
wrd2cnt1 = {}
value = "" 
key = ""
final_1 = dict()
# input comes from STDIN
for line1 in sys.stdin:
	# remove leading and trailing whitespace
	line1 = line1.strip()
	if(line1):
		words = line1.split('\t')
		if words[0] != '~':
			if words[0][-1] == '~':
  				idn = words[1]
				if idn not in final_1:
					final_1[idn] = dict()
				if words[0][:-2] == key :
	               		 	final_1[idn][words[0][:-2]] = value
			else:
				key = words[0]
				value = words[1]

#print final_1
for i in final_1:
        d=dict()
        d[i] = final_1[i]
        print str(d)
