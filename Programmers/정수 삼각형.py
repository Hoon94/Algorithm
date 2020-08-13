def solution(triangle):
    m_lst = []

    for row in triangle:
        lst = []

        if len(m_lst) == 0:
            lst.append(row[0])
        else:
            for idx, num in enumerate(row):
                if idx == 0:
                    lst.append(m_lst[-1][idx] + num)
                elif idx == len(row)-1:
                    lst.append(m_lst[-1][-1] + num)
                else:
                    lst.append(max(m_lst[-1][idx - 1],m_lst[-1][idx]) + num)
        
        m_lst.append(lst)
    
    return max(m_lst[-1])

if __name__ == "__main__":
    
    #Test case 1
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    #result 30

    print(solution(triangle))