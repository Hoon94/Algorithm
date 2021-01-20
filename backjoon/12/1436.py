N = int(input())
series = []
i = 666

while len(series) < 10001:

    if "666" in str(i):
        series.append(i)

    i += 1

print(series[N-1])

'''
다른 풀이법

N = int(input())
movie = 666

while N:
    if "666" in str(movie):
        N -= 1
    movie += 1

print(movie - 1)

'''