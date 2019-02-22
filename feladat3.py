#!/usr/bin/python
#feladat 3

def alarm_clock(day, holiday):
	weekday = range(0,5)
	weekend = range(5,7)
	if(day in weekday):
		if holiday == False:
			return '7:00'
		else:
			return '10:00'
	elif(day in weekend):
		if holiday == False:	
			return '10:00'
		else:
			return 'OFF'
	else:
		return "ERROR"

for idx in range(0,9):
	print('A het ' + str(idx) + ". e(a)dik napjan ebreszt vakacioban: " + alarm_clock(idx, True))
	print('A het ' + str(idx) + ". e(a)dik napjan ebreszt munkaidoben: " + alarm_clock(idx, False))