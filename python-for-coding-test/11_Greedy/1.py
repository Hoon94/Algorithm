n = int(input())
scare = list(map(int, input().split()))
group = 0
member = 0

scare.sort()

for i in range(n):
    if member + 1 == scare[i]:
        group += 1
        member = 0
    else:
        member += 1

print(group)
