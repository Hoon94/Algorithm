def count(string):
	word = string.split()
	delimiter = string.split(',')
	line = string.split('\n')

	print('word :', len(word), 'delimiter :', len(delimiter) - 1, 'line :', len(line))

string = input('Put string : ')
count(string)
