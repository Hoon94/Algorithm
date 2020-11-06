import sys
input = sys.stdin.readline

if __name__ == "__main__":
    
    n, k = map(int, input().split())
    nums = list(input().strip())
    answer, remain = [], k
    
    for i in range(n):
        while remain and answer and answer[-1] < nums[i]:
            answer.pop(-1)
            remain -= 1

        answer.append(nums[i])

    print(''.join(answer[:n - k]))