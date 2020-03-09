a = input()
a = a.upper()
b = []

alpha = list(map(chr, range(65, 91)))

for i in range(26):
    b.append(a.count(alpha[i]))

if b.count(max(b)) == 1:
    print(alpha[b.index(max(b))])
else:
    print('?')