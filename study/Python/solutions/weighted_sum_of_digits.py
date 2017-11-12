import math

n = int(input())
v = input().split()

for i in range(n):
	sums = int(v[i])

	# judge the digits of sums
	# if (sums % 10) == 0:
	# 	digs = math.ceil(math.log10(sums)) + 1
	# else:
	# 	digs = math.ceil(math.log10(sums))

	if (sums == 0):
		digs = 1
	else:
		digs = math.ceil(math.log10(sums))

	dig_array = [0 for i in range(digs)]
	for j in range(digs):
		dig_array[j] = sums % (10**(j+1)) // 10**(j) 

	digsum = 0
	for j in range(digs):
		digsum += dig_array[-(j+1)] * (j+1)
	print(digsum, end=" ")