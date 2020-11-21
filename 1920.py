import sys
input = sys.stdin.readline

if __name__ == "__main__":

    n = int(input())
    n_list = set(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))

    for _ in m_list:
        if _ in n_list:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')