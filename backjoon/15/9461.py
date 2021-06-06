import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    N = int(sys.stdin.readline())
    seq = [1, 1, 1, 2, 2]

    if N > 5:
        for j in range(5, N):
            seq.append(seq[j - 1] + seq[j - 5])

    print(seq[N - 1])
