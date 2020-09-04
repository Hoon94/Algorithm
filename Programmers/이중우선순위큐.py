import heapq

def solution(operations):
    answer = []
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