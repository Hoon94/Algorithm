def to_Celsius_degree(F):
	C = (F - 32)*5/9
	return C

if __name__ == '__main__':
	F = float(input('Fahrenheit degree : '))
	result = to_Celsius_degree(F)
	print(result)
