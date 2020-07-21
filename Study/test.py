array = [[0] * 5] * 5
print(array)
array[3][1] = 4 
print(array)
print(type(array))

cache = [[0 for y in range(5)] for x in range(5)]
print(cache)
cache[3][1] = 4
print(cache)