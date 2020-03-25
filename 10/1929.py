m, n = map(int, input().split())
num = [2]

for i in range(3, n+1):
    j = 0
    flag = 0

    for j in range(len(num)):
        if i % num[j] == 0:
            flag = 0
            break
        flag = 1

    if flag == 1:
        num.append(i)
        if i >= m:
            print(i)