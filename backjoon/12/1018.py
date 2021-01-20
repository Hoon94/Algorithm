N, M = map(int, input().split())
map_list = [list(input()) for _ in range(N)]

min_num = []

for i in range(N - 7):
    for j in range(M - 7):
        num1, num2 = 0, 0
        # White
        for k in range(i, i+8):
            for l in range(j, j+8):
                if((k + l - i - j)%2 == 0):
                    if (map_list[k][l] == 'B'):
                        num1 += 1
                else:
                    if (map_list[k][l] == 'W'):
                        num1 += 1
    
        # Black
        for k in range(i, i+8):
            for l in range(j, j+8):
                if((k + l - i - j)%2 == 0):
                    if (map_list[k][l] == 'W'):
                        num2 += 1    
                else:
                    if (map_list[k][l] == 'B'):
                        num2 += 1

        min_num.append(min(num1, num2))

print(min(min_num))