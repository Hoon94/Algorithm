a = input()
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in range(len(b)):
    for j in b:
        if j in a:          
            a = a.replace(j,'a')

print(len(a))