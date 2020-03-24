a = int(input())
b = list(map(int, input().split()))
count = 0

for i in range(a):
    j = 2
    if b[i] == 1:
        count += 1
    else:
        while b[i]//j > 0 and b[i] > j:
            if b[i]%j == 0:
                count += 1
                break
            j += 1

print(len(b) - count)