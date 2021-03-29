def solution(s):
    answer = float("INF")
    l = len(s) // 2
    count = 1

    if len(s) <= 1:
        return len(s)

    for i in range(1, l + 1):
        string = ''
        for j in range(i, len(s), i):
            if s[j-i:j] == s[j:j+i]:
                count += 1
            else:
                string += str(count) + s[j-i:j] if count > 1 else s[j-i:j]
                count = 1
        else:
            string += str(count) + s[j-i:j] if count > 1 else s[j:j+i]
            count = 1

        # print(string)
        answer = min(answer, len(string))

    return answer
