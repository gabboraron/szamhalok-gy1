#!/usr/bin/python
#feladat 4

def fib(nr):
	if (nr == 0):
		return 0
	elif (nr == 1):
		return 1
	else:
		return fib(nr-1)+fib(nr-2);

for x in range(1,10):
	print(str(x) + ": " + str(fib(x)))