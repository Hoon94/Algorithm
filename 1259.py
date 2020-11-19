import sys
input = sys.stdin.readline

if __name__ == "__main__":

    while True:
        num = input().strip()
        check = len(num) // 2

        if num == '0':
            break
        elif check == 0:
            print("yes")
        else:
            for i in range(check):
                if num[i] != num[-1 - i]:
                    print("no")
                    break
                elif i == check - 1:
                    print("yes")