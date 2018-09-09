#!/usr/bin/env python
import sys
 
# maps words to their counts
wrd2cnt1 = dict()
tot = 0
# input comes from STDIN
for line1 in sys.stdin:
    # remove leading and trailing whitespace
    line1 = line1.strip()
    tot = tot + 1
    # parse the input we got from mapper.py
    k, cnt = line1.split('\t')
    # convert cnt (currently a string) to int
    try:
        cnt = int(cnt)
    except ValueError:
        continue
    try:
       	wrd2cnt1[k] = [wrd2cnt1[k][0]+1,wrd2cnt1[k][1]+cnt]
    except:
       	wrd2cnt1[k] = [1,cnt]
 
# write the tuples to stdout
# Note: they are unsorted
print wrd2cnt1
