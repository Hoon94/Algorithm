from copy import deepcopy

def sm(b):
    b += 1
    if b == 10:
        return b
    print('sm : ', b)
    return sm(b)

def s(a):

    for i in range(2):
        d = sm(a)
        print('s : ', a)
    return d 

if __name__ == "__main__":
    a = 3
    print(s(a))