#!/usr/bin/env python
import sys
import math

clas = open('classes.txt','r')
cla=dict()
for i in clas.readlines():
    cla.update(eval(i))

m = 1
w = 1050054
cnt = 0
tot = 0
tot_no_class = 0
for i in cla:
    tot_no_class = tot_no_class + cla[i][0]
for line1 in sys.stdin:
	line1 = line1.strip()
	test = eval(line1)
	for i in test:
    		m_prob = -2147483647
    		m_class = ""
    		for c in cla:
        		prb = math.log(float(cla[c][1]+ (float(m)/w))/ (tot_no_class+1))
        		for word_fina_1 in test[i]:
            			j = 1
				if c in eval(test[i][word_fina_1]):
                			j = j + int(eval(test[i][word_fina_1])[c])
	       			prb = prb + math.log((float(j)+(float(m)/w))/(cla[c][1]+ m))
        		if prb > m_prob:
            			m_prob = prb
            			m_class = c
    	if m_class in i[len(i.split(' ')[0])+1:].split(','):
        	print "1"
    	else:
		print "0"
