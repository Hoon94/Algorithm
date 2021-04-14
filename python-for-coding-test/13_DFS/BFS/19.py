n = int(input())
sequence = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_val, min_val = -float("INF"), float("INF")


def cal(i, operand1, operand2):
    if i == 0:
        return operand1 + operand2
    elif i == 1:
        return operand1 - operand2
    elif i == 2:
        return operand1 * operand2
    else:
        return int(operand1 / operand2)
        # return operand1 // operand2


def dfs(answer, index):
    global max_val
    global min_val
    if index == len(sequence):
        max_val = max(max_val, answer)
        min_val = min(min_val, answer)

    for i in range(4):
        if operator[i] == 0:
            continue

        operator[i] -= 1
        dfs(cal(i, answer, sequence[index]), index + 1)
        operator[i] += 1


dfs(sequence[0], 1)

print(max_val)
print(min_val)
