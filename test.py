import queue

data = queue.PriorityQueue()

data.put((10, 5))
data.put((3, 10))
data.put((9, 1))

print(data.qsize())
print(data.get())