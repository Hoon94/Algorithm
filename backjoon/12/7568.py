N = int(input())
a_list = []

for i in range(N):
    a = list(map(int, input().split()))
    a_list.append(a)

for i in range(N):
    score = 1
    for j in range(N):
        if a_list[i][0] < a_list[j][0] and a_list[i][1] < a_list[j][1]:
            score += 1
    
    print(score, end=' ')