a = int(input())

'''
for i in range(a):
    print()
    for j in range(i+1):
        print("*", end='')
'''

for i in range(a):
    print(' '*(a-i-1)+'*'*(i+1))