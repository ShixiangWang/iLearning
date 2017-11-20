# function:
# A file containing all the even-numbered lines
# from the original file. Assume 1-based numbering 
# of lines.

with open('E:/Github/iPython/study/Python/bioinfo/readfile_evenLines.txt', 'r') as f:
	i = 1
	for line in f.readlines():
		if i%2 == 0:
			print(line.strip())
			i += 1
		else:
			i += 1


