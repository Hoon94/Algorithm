a = input().lower()
s =  ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
sec = 0

for i in range(len(a)):
    for j in s:
        if a[i] in j:
            sec = sec + s.index(j) + 3
    
print(sec)