def solution(tri):
    m_lst = []

    for row in tri:
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