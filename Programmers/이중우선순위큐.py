import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]

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