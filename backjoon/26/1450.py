import sys
import bisect
input = sys.stdin.readline

n, c = map(int, input().split())
w = list(map(int, input().split()))
sep = n // 2
w1, w2 = w[:sep], w[sep:]
wl, wr = [], []


def bf(arr, seq, idx, summ):
    if len(arr) == idx:
        seq.append(summ)
        return seq

    bf(arr, seq, idx + 1, summ)
    bf(arr, seq, idx + 1, summ + arr[idx])

    return seq


wl = bf(w1, wl, 0, 0)
wr = sorted(bf(w2, wr, 0, 0))
r = 0

for i in wl:
    if c - i < 0:
        continue

    idx = bisect.bisect_right(wr, c - i)
    r += idx

print(r)
