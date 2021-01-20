a = list(input().split())

for i in range(len(a)):
    temp = ''
    for j in range(len(a[i])):
        temp = temp + a[i][-j-1]
    a[i] = temp

print(max(a))