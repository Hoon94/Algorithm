import sys

N = int(sys.stdin.readline())
order = list()

for i in range(N):
    order.append(int(sys.stdin.readline()))

#order.sort()

for _ in sorted(order):
    sys.stdout.write(str(_) + '\n')

#파이썬은 기본 정렬 함수가 O(nlog(n))으로 구성.
#merge sort, heap sort를 사용하지 않아도 된다.