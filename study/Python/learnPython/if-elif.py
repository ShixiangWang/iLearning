# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

BMI = weight/(height**2)

info = "小明体重"
if BMI < 18.5:
	print(info, "过轻")
elif BMI <= 25 and BMI >= 18.5:
	print(info, "正常")
elif BMI > 25 and BMI <=28:
	print(info, "肥胖")
else: 
	print(info, "严重肥胖")