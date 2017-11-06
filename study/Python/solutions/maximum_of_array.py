array = input().split()
mi = int(array[1])
ma = int(array[1])
for i in array:
	v = int(i)
	if v < mi:
		mi = v
	if v > ma:
		ma = v

print(ma,mi)
