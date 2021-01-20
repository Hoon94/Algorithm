import sys
import heapq

if __name__ == "__main__":
    
    heap = []

    for _ in range(int(input())):
        num = int(sys.stdin.readline())
        
        if num != 0:
            heapq.heappush(heap, num)
        else:
            try: # if heap:
                print(heapq.heappop(heap))
            except: # else:
                print(0)