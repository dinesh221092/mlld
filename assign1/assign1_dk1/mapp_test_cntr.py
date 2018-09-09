#!/usr/bin/env python
import sys

cnt = 0
#--- get all lines from stdin ---
for line1 in sys.stdin:
    #--- remove leading and trailing whitespace---
    line1 = line1.strip()
    cnt = cnt + 1
    #--- split the line1 into words ---
    words = line1.split()
    #--- output tuples [word_fina_1, 1] in tab-delimited format---
    for word_fina_1 in words[1:]:
        print word_fina_1+' ~'+'\t'+str(cnt)+' '+words[0]
