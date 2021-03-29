s = list(input())
s.sort()
i = 0
num = 0

while s[i].isdigit():
    num += int(s[i])
    i += 1
else:
    s.append(str(num))

print(''.join(s[i:]))
