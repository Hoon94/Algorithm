a = int(input())

num = 0
#before = 0
room = 0
j = 1

while True:
    before = num
    num += 1 * j
    room += 1
    if a <= num:
        break
    j += 1

if room%2 == 1:
    print('{}/{}'.format(num - a + 1, a - before))
else:
    print('{}/{}'.format(a - before, num - a + 1))