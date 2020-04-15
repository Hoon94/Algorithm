N = int(input())
a = 0

while True:
    a_list = list(map(int, str(a)))
    result = 0

    for i in range(len(a_list)):
        result += a_list[i]
    
    result = result + a

    if result == N:
        print(a)
        break
    elif N == a:
        print(0)
        break

    a += 1