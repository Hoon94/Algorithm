import sys

a = int(sys.stdin.readline())
value = 0
score = 0

for i in range(a):
    b = list(sys.stdin.readline())
    for j in range(len(b)):
        if b[j] == 'O':
            value = value + 1
            score = score + value
        else:
            value = 0
    print(score)
    score = 0
