if __name__ == '__main__':
	file = open('alkaline_metals.txt', 'r')
	lines = file.readlines()
	result = []
	#fin = []
	#all = []
	#i = 0
	for line in lines: 
		result.append(line.split())
#		result.append([float(x) for x in line.split()])
	#n = len(result)
	#for x in range(n):
	#	fin.append([int(x) in result[i][0])
	#	fin.append([float(y) in result[i][1]])
	#	all.append(fin)
	#	fin = []
	#	i = i + 1
		#result.append([int(line.split()[0]),float(line.split()[1])]) #이렇게 해도 되는 것 같아요

	print(result)
