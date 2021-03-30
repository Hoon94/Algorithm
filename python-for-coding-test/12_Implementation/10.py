key = [[0, 0], [1, 0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)

    def rotattion(key, m):
        answer = []

        for i in range(m):
            r_list = []
            for j in range(1, m + 1):
                r_list.append(key[-j][i])

            answer.append(r_list)

        return answer

    for _ in range(1):
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    for l in range(m):
                        print(i, j, k, l)
                        print(key[k][l], lock[i+k][j+l])
                # if key[i+j][j+k] + lock[i+j][j+k] != 1:
                #     break

    return answer


solution(key, lock)

# 010 100 100
# 110 001 000
