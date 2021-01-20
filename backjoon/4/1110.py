a = input()
i = 0

if int(a) < 10:
    b = [0, int(a)]
else:
    b = [int(a[0]), int(a[1])]

while True:
    num = str(b[0]+b[1])
    value = b[1]*10 + int(num[-1])
    i = i + 1
    if value == int(a):
        break
    temp = int(num[-1])
    b[0] = b[1]
    b[1] = temp

print(i)