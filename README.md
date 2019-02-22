# GY2
## Általános infó
* A python `2.x` ajánlott a `3.x` helyett.
* Linux ajánlott windowsal szemben. (amúgyis :) )

## Python alapok
`#!/usr/bin/python` kell a fájl elejére
A `#` megjegyzs sort jelöl

### Ciklus
````PYTHON
x = 1
for i in range(1,10):
	x += i
	print(str(i) + " : " + str(x))
  ````
### Adatszerkezetek
````Python
mylist = [idx*idx for idx in range(0,10)]
print(mylist)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

mydict = {i:i*i for i in range(0,5) if i != 2}
print(mydict)
#{0: 0, 1: 1, 3: 9, 4: 16}

mytuple = tuple(j*j for j in range(0,3))
print(mytuple)
#(0, 1, 4)
````

### Függvények
````Python
def even(number):
	if((number % 2) == 0):
		return True
	else:
		return False

for x in range(1,10):
	if (even(x)):
		print("paros: " + str(x))
````

**Vagy **

````Python
def complex(x):
	return x**2, x**3, x**4
print(complex(2))

a, b, c = complex(2)
print(a,b,c)

_, rv, _ = complex(2)
print(rv)
````

### Lambda függvények
````Python
is_even = lambda num: (num%2) == 0
is_even2 = lambda num: True if (num%2) == 0 else False

for i in range(1,10):
	if (is_even(i)):
		print("paros: " + str(i))
````
### Map
````Python
def fahrenheit(T):
	return((float(9)/5)*T+32)

def celsius(T):
		return (float(5)/9)*(T-32)	

temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celsius, F)

temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))

print("F: ")
print(temperatures_in_Fahrenheit)
print("C: ")
print(temperatures_in_Celsius)
````

### Filterek
````Python
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x%2, fibonacci))

print(odd_numbers)
````

### Fájlkezelés
Tömböket ad soronként: 
````Python
with open('alma.txt', 'r') as f:
	for line in f:
		print(line.rstrip('\n').split(','))

ff = open("demo.txt", "r")
````
Az egészet soronként kiolvassa:
````Python
print(f.read())
````
Egy sort olvas csak:
````Python
print(f.readline())
````
Mindnet olvas sorban:
````Python
for x in f:
    print(x)
````
Írás fájlba:
`w`- write 
`a`- append
````Python
with open ('korte.txt', "w") as korte:
	korte.write("bla bla blablabla")
````
### Ester egg
````Python
import this
````

## Feladatok
### Feladat1
> Írjunk függvényt ami megadja egy bemenetben kapott évszámról, hogy szökőév-e. Egy év szökőév, ha osztható néggyel, de akkor nem, ha osztható százzal, hacsak nem osztható négyszázzal. Példák: 1992,1996,2000,2400 szökőév, de 1993, 1900 nem.

````Python
def szokoev(x):
	if(((x%4) == 0) and ((x%100) != 0)):
		return True
	elif((x%400) == 0):
		return True
	else:
		return False

if szokoev(2012):
	print("2012 szokoev")
````
#### Feladat3
> A hét napjait jelöljük 0-6-ig (Hétfő,...,Vasárnap). Írjunk egy függvényt, ami megadja mikor kell kelnünk az adott napon (hétköznap ’7:00’ hétvégén ’10:00’), kivéve ha vakációzunk, mert akkor hétköznap ’10:00’ hétvégén ’OFF’

````Python
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
````

### Feladat4
> Írjunk függvényt ami megadja az n. fibonacci számot
````Python
def fib(nr):
	if (nr == 0):
		return 0
	elif (nr == 1):
		return 1
	else:
		return fib(nr-1)+fib(nr-2);

for x in range(1,10):
	print(str(x) + ": " + str(fib(x)))
````
