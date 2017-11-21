n = int(input())
for i in range(n):
	array = [int(i) for i in input().split()]
	print(round(sum(array[0:-1])/(len(array)-1)), end=" ") 