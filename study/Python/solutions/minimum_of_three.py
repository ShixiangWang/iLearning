n = int(input())
for i in range(n):
	a,b,c=input().split()
	a = int(a)
	b = int(b)
	c = int(c)
	min3 = int(0)
	if a > b:
		min3 = b
	else:
		min3 = a
	if min3 > c:
		min3 = c
	print(min3)

