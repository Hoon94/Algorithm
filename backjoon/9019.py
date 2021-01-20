T = int(input())
result = list()

for i in range(T):
    A, B = map(int, input().split())

    alist = list(map(int, str(A).zfill(4)))
    blist = list(map(int, str(B).zfill(4)))
#'''
    while alist != blist:
        if sorted(alist) == sorted(blist):
            alist.append(alist.pop(0))
            result.append('L')
        


print(''.join(result))
#'''

#print(blist)