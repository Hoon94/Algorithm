import sys

a = int(sys.stdin.readline())
count = 1
word = 0

for i in range(a):
    b = sys.stdin.readline()
    for j in range(len(b)-1):
        if b[j] == b[j+1]:
            count = count + 1
        elif b.count(b[j]) != count:
            count = 1
            word = word + 1
            break
        else:
            count = 1

print(a - word)