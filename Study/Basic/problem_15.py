import convert_temp

if __name__ == '__main__':
	k = input('Temperature : ')

	if 'C' in k:
		k = k.replace('C','')
		print(str(convert_temp.C2F(k)) + 'F', str(convert_temp.C2K(k)) + 'K')
	
	if 'K' in k:
		k = k.replace('K','')
		print(str(convert_temp.K2F(k)) + 'F', str(convert_temp.K2C(k)) + 'C')

	
	if 'F' in k:
		k = k.replace('F','')
		print(str(convert_temp.F2C(k)) + 'C', str(convert_temp.F2K(k)) + 'K')
