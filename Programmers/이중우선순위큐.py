import heapq

def solution(operations):
    heap = []
    
    for op in operations:
        order = op.split()

        if order[0] == 'I':
            heapq.heappush(heap, int(order[1]))
        elif heap:       
            if order[1] == '1':
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)
                
    if len(heap) == 0:
        return [0, 0]
    
    return [max(heap), min(heap)]

if __name__ == "__main__":
    
    '''
    #Test case 1
    operations = ["I 16", "D 1"]
    #result [0, 0]
    '''

    #Test case 2
    operations = ["I 7", "I 5", "I -5", "D -1"]
    #result [7, 5]

    print(solution(operations))