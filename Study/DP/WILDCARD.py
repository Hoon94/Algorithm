def wildcard(w, name):
    #기저 사례 처리
    if w == name:
        return name
    
    if '*' in name:
        point = name.index('*')
        name = wildcard(w[:point], name[:point]) + name[point] + wildcard(w[point + 1:], name[point + 1:])

    #if '?' in name:
    #    point = name.index('?')
        
        
    return name

answer = wildcard('he*p*a', 'help2a')
print(answer)

'''
#Test case
3

he?p
3
help
heap
helpp

*p*
3
help
papa
hello

*bb*
1
babbbc
'''