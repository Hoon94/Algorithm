a = int(input())
room = 1
num = 1
i = 1

if a == 1:
    print(a)
else:
    while True:
        num += 6 * i
        room += 1
        if(a <= num):
            break
        i += 1
    print(room)