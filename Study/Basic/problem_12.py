import math

def pathlength(x, y):
	n = len(x)-1
	for i in range(n):
		sum = math.sqrt(math.pow(x[i+1]-x[i],2)+math.pow(y[i+1]-y[i],2))
		print (i)
	return sum

if __name__ == '__main__':
	x = [1, 2, 1, 1]
	y = [1, 1, 2, 1]
	print(pathlength(x, y))
