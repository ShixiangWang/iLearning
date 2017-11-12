import math

n = int(input())
for i in range(n):
	a,b,c=input().split()
	a = int(a)
	b = int(b)
	c = int(c)
	sums = (a * b) + c

	# judge the digits of sums
	digs = math.ceil(math.log10(sums)) + 1

	digsum = 0
	for  j in range(digs):
		digsum = (sums % (10**(j+1)) // 10**(j) ) + digsum

	print(digsum, end=" ")