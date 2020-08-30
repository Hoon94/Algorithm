def pack(capacity, item):
    if item == n:
        return 0

    if cache[capacity][item] != -1:
        return cache[capacity][item]

    cache[capacity][item] = pack(capacity, item + 1)

    if capacity >= volume[item]:
        cache[capacity][item] = max(cache[capacity][item], pack(capacity - volume[item], item + 1) + need[item])

    return cache[capacity][item]

def reconstruct(capacity, item):
    global num
    if item == n:
        return

    if pack(capacity, item) == pack(capacity, item + 1):
        reconstruct(capacity, item + 1)
    else:
        #print(name[item])
        res[num] = name[item]
        num += 1
        reconstruct(capacity - volume[item], item + 1)

if __name__ == "__main__":
    '''
    n = 6
    capacity = 10
    num = 0

    volume = [4, 2, 6, 4, 2, 10]
    need = [7, 10, 6, 7, 5, 4]

    cache = [[-1 for x in range(7)] for y in range(11)]
    name = ['laptop', 'camera', 'xbox', 'grinder', 'dumbell', 'encyclopedia']

    res = ['none'] * 6
    '''
    
    n = 6
    capacity = 17
    num = 0

    volume = [4, 2, 6, 4, 2, 10]
    need = [7, 10, 6, 7, 5, 4]

    cache = [[-1 for x in range(7)] for y in range(capacity + 1)]
    name = ['laptop', 'camera', 'xbox', 'grinder', 'dumbell', 'encyclopedia']

    res = ['none'] * 6

    print(pack(capacity, 0))
    reconstruct(capacity, 0)
    for i in range(num):
        print(res[i])