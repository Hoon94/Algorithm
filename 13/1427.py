N = list(map(int, str(input())))

N.sort()
N.reverse()

for i in N:
    print(i, end='')