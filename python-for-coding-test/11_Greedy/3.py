s = list(map(int, input()))
zero, one = 0, 0
if s[0] == 0:
    zero = 1
else:
    one = 1

for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        if s[i] == 1:
            one += 1
        else:
            zero += 1

answer = min(zero, one)

print(answer)
