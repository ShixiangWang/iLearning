nums = input().split()
n = int(nums[0])
cor = (212-32)/100
for i in range(n):
	f = int(nums[i+1])
	c = round((f-32)/cor)
	print(c,end=" ")