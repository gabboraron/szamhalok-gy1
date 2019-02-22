#!/usr/bin/python
#feladat 1
def szokoev(x):
	if(((x%4) == 0) and ((x%100) != 0)):
		return True
	elif((x%400) == 0):
		return True
	else:
		return False

if szokoev(2012):
	print("2012 szokoev")