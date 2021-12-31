alphabet = [0] * 26
s = input()
list_s = list(s)

for i in list_s:
    alphabet[ord(i) - 97] = alphabet[ord(i) - 97] + 1

print(str(alphabet).replace('[', '').replace(',', '').replace(']', ''))
