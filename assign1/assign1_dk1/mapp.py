#!/usr/bin/env python
import sys
import re
l=list()
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
#--- get all lines from stdin ---
for line1 in sys.stdin:
    #--- remove leading and trailing whitespace---
    line1 = line1.strip()

    #--- split the line into words ---
    words = line1.split()
    if(line1):
        key = words[0]

    #--- output tuples [word, 1] in tab-delimited format---
    for s in words[1:]:
        print(re.sub(r'[^\w\s]','',s)+'\t'+ key)
	
