import sys

try:
    while True:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
except:
    pass #exit()

'''
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)
'''