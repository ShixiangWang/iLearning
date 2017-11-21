n = int(input())
for i in range(n):
	weight,height=input().split()
	weight = float(weight)
	height = float(height)
	BMI = weight / (height ** 2)
	if BMI < 18.5:
		print("under", end=" ")
	elif BMI >= 18.5 and BMI < 25.0:
		print("normal", end=" ")
	elif BMI >= 25.0 and BMI < 30.0:
		print("over", end=" ")
	else:
		print("obese", end=" ")


