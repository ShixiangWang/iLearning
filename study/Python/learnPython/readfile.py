with open('E:/Github/iPython/study/Python/learnPython/test_file.txt', 'r') as f:
	print(f.read())

with open('E:/Github/iPython/study/Python/learnPython/test_file.txt', 'a') as f:
	f.write('\nHello, world!')

with open('E:/Github/iPython/study/Python/learnPython/test_file.txt', 'r') as f:
	print(f.read())
