# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	# check data type of a,b,c
	if not isinstance(a, (int, float)):
		raise TypeError("bad operand type")
	if not isinstance(b, (int, float)):
		raise TypeError("bad operand type")
	if not isinstance(c, (int, float)):
		raise TypeError("bad operand type")

	# check value of a
	if a == 0:
		raise TypeError("a can't be zero")
	elif (b*b - 4*a*c) <0:
		return(print("There is no solution."))
	else:
		x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
		x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
		return (x1,x2)

print(quadratic(2,3,1))
print(quadratic("a",3,1))
