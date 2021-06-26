def gcd(x, y):
    mod = x % y

    while mod > 0:
        x = y
        y = mod
        mod = x % y

    return y


def lcm(x, y):
    return x * y // gcd(x, y)


a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))
