n = int(input())
rad = list(map(int, input().split()))

for i in range(n - 1):
    x = rad[0]
    y = rad[i + 1]

    while(x % y != 0):
        r = x % y
        x = y
        y = r

    denom = rad[0] // y
    numer = rad[i + 1] // y

    print(f'{denom}/{numer}')
