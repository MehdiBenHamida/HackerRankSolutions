#!/bin/python

import sys


n = int(raw_input().strip())
k = list(xrange(n))
l = []
for i in xrange(n):
	l.append(map(int, raw_input().strip().split(' ')))
for i in xrange(n):
	l[i]=list((set(k) - set(l[i]))-set([i]))
x = []
for i in xrange(n):
	for j in xrange(len(l[i])):
		x.append(l[i][j])
x = list(set(x))
s = len(list(set(k)-set(x)))
print (s)


'''i = 0
while i < n:
	#if len(l[i])==0:
	#	del l[i]
	if len(l[i])==1:
		for j in xrange(n):
			l[j]=list(set(l[j])-set(l[i]))
		del l[i]
		n = n - 1
	print l
	i = i + 1
print len(l)'''
