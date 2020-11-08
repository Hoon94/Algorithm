import random

def qsort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    left = [ item for item in data[1:] if pivot > item ]
    right = [ item for item in data[1:] if pivot <= item ]
    
    return qsort(left) + [pivot] + qsort(right)

if __name__ == "__main__":
    data_list = random.sample(range(100), 10)
    print (qsort(data_list))