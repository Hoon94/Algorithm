import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def merge_sort(start, end):
    global swap, arr
    size = end - start
    mid = (start + end) // 2
    if size <= 1:
        return

    merge_sort(start, mid)
    merge_sort(mid, end)

    new_arr = []
    idx1, idx2 = start, mid
    cnt = 0
    while idx1 < mid and idx2 < end:
        if arr[idx1] > arr[idx2]:
            new_arr.append(arr[idx2])
            idx2 += 1
            cnt += 1
        else:
            new_arr.append(arr[idx1])
            idx1 += 1
            swap += cnt

    while idx1 < mid:
        new_arr.append(arr[idx1])
        idx1 += 1
        swap += cnt

    while idx2 < mid:
        new_arr.append(arr[idx2])
        idx2 += 1

    for t in range(len(new_arr)):
        arr[start + t] = new_arr[t]


n = int(input())
arr = list(map(int, input().split()))
swap = 0
merge_sort(0, n)
print(swap)
