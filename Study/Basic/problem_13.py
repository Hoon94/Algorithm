import math

def pathlength(x, y):
	length = 0
	for i in range(len(x) - 1):
		length = length +((x[i] - x[i+1])**2+(y[i]-y[i+1])**2)**0.5
	return math.pi-length

if __name__ == '__main__':
	for k in range(2, 11):
		x = list()
		y = list()
		N = 2 * k
		print('N = ' + str(N) + ' error', end = '')
		for i in range(N+1):
			x.append(1/2*math.cos((2*math.pi*i)/N))
			y.append(1/2*math.sin((2*math.pi*i)/N))
		print(pathlength(x,y))
