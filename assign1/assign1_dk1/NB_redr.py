#!/usr/bin/env python
import sys
 
# maps words to their counts
cnt = 0
tot = 0
for prbline1 in sys.stdin:
	tot = tot + 1
	prbline1 = prbline1.strip()
	if int(prbline1) == 1:
		cnt = cnt + 1
print (cnt*100)/tot
