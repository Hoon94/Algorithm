def is_even(k):

	while k > 1:
		k = k - 2
	if k == 0:
		print('True')
	else:
		print('False')

k = int(input('k : '))
is_even(k)
