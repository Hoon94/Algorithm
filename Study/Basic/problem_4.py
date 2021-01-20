if __name__== "__main__":
	a = [1, 2, 3]
	b = [9, 8, 7]
	c = []
	n = len(a)

	for i in range(0,n):
		c.append(a[i] * b[i])

	print('list c : ', c)
