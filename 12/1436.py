N = int(input())
series = []
i = 666

while len(series) < 10001:

    if "666" in str(i):
        series.append(i)

    i += 1

print(series[N-1])