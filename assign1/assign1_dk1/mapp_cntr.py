#!/usr/bin/env python
import sys

#--- get all lines from stdin ---
for line1 in sys.stdin:
    #--- remove leading and trailing whitespace---
    #line1 = line1.strip()

    #--- split the line1 into words ---
    words = line1.split()
    if(line1):
         key = words[0].split(',')
	 for k in key:
	 	print k +'\t'+str(len(words[1:]))
