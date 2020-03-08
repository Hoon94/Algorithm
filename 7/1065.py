import sys

def single(a: int):
    diff = 0
    a_list = list(map(int, str(a).zfill(2)))
    diff = a_list[0] - a_list[1]
    
    for i in range(len(a_list)-1):
        b = a_list[i] - a_list[i+1]
        if diff != b:
            return 0
    return 1

a = int(sys.stdin.readline())
count = 0

for i in range(a):
    count = single(i+1) + count

print(count)