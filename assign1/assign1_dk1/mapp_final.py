#!/usr/bin/env python
import sys
 
#--- get all lines from stdin ---
for line1 in sys.stdin:
	#--- remove leading and trailing whitespace---
	line1 = line1.strip()
	print line1		
