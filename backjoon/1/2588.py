a = input()
b = input()
sum = 0

for i in range(len(b)):

    value = int(a) * int(b[-(i+1)])
    print(value)
    sum = sum + (value * (10**i))

print(sum)