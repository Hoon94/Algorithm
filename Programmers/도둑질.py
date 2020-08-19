def solution(money):
    x1, y1, z1 = money[0], money[1], money[0] + money[2]
    x2, y2, z2 = 0, money[1], money[2]

    for i in money[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1) + i
        x2, y2, z2 = y2, z2, max(x2, y2) + i
    return max(x1, y1, y2, z2)

if __name__ == "__main__":
    
    #Test case 1
    money = [1, 2, 3, 1]
    #result 4

    print(solution(money))