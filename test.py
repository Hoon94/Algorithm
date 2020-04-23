import sys

N = int(sys.stdin.readline())
arr = []
count = 0

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

#3 최빈값
from collections import Counter
k=Counter(arr).most_common()
print(k)

if len(arr) > 1:  #만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
    if k[0][1] == k[1][1]:
        print(k[1][0]) 
    # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
    else: 
        print(k[0][0]) 
else: 
    print(arr[0])