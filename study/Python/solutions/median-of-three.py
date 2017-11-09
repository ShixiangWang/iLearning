n = int(input())
for i in range(n):
	a,b,c=input().split()
	a = int(a)
	b = int(b)
	c = int(c)
	# set a default value as mid
	t = int(0)
	# sort a,b,c from small to big
	if a > b:
		t = b
		b = a
		a = t
	if b > c:
		t = c
		c = b
		b = t
	if a > b:
		t = b
		b = a
		a = t
	print(b, end=" ")

