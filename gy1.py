#!/usr/bin/python

#for ciklus
x = 1
for i in range(1,10):
	x += i
	print(str(i) + " : " + str(x))

#adatszerkezetek
mylist = [idx*idx for idx in range(0,10)]
print("mylist: ")
print(mylist)

mydict = {i:i*i for i in range(0,5) if i != 2}
print("mydict: ")
print(mydict)

mytuple = tuple(j*j for j in range(0,3))
print("mytuple: ")
print(mytuple)

#fuggvenyek
def even(number):
	if((number % 2) == 0):
		return True
	else:
		return False

for x in range(1,10):
	if (even(x)):
		print("paros: " + str(x))

#fuggvenyek2
def complex(x):
	return x**2, x**3, x**4
print(complex(2))

a, b, c = complex(2)
print(a,b,c)

_, rv, _ = complex(2)
print(rv)

#lambda
is_even = lambda num: (num%2) == 0
is_even2 = lambda num: True if (num%2) == 0 else False

for i in range(1,10):
	if (is_even(i)):
		print("paros: " + str(i))

#map
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

#filter
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x%2, fibonacci))

print(odd_numbers)

#fajlkezeles
with open('alma.txt', 'r') as f:
	for line in f:
		print(line.rstrip('\n').split(','))		#tombbe rakva adja vissza

ff = open("demo.txt", "r")
#print(ff.read())								#az egeszet soronkent kiolvassa
#print(ff.readline())							#egy sort olvas

for x in ff:
	print(x)									#mindent olvas sorban


with open ('korte.txt', "w") as korte:	#w-write | a- append
	korte.write("bla bla blablabla")



#easter egg
import this
