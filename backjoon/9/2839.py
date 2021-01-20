a = int(input())

done = False

for i in range(a//3 + 1):
    for j in range(a//5 + 1):
        if(a == 3*i + 5*j):
            done = True
            break
    if(done == True):
        break
if done == False:
    print(-1)
else:
    print(i+j)