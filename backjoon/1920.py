import sys
input = sys.stdin.readline
print = sys.stdout.write

if __name__ == "__main__":

    n = int(input())
    n_list = set(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))

    for _ in m_list:
        print('1\n') if _ in n_list else print('0\n')