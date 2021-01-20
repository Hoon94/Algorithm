N = int(input())
a = 0

for i in range(1, N + 1):
    a_list = list(map(int, str(i)))

    a = i + sum(a_list)

    if a == N:
        print(i)
        break
    elif N == i:
        print(0)
        break