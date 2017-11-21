n = int(input())
for i in range(n):
	# a is the first value of the sequence
	# b is the step size
	# c is the number of first value should be accounted
	a,b,c=input().split()
	a = int(a)
	b = int(b)
	c = int(c)

	sums = 0
	for i in range(c):
		sums += a + i*b

	print(sums, end=" ")

