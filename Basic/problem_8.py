def avg_populations():
	eastern_Asia = ['China', 'DPR_Korea', 'Hong_Kong', 'Mongolia', 'Republic_of_Korea', 'Japan', 'Taiwan']
	populations = [1500, 33, 7, 45, 49, 101, 21]

	n = len(eastern_Asia)
	sum = 0

	for i in range(n):
		sum = populations[i] + sum
	
	return sum/n

print(avg_populations())
