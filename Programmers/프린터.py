def solution(priorities, location):
    pos = []

    for i in range(len(priorities)):
        if i == location:
            pos.append(True)
        else:
            pos.append(False)

    answer = 0
    count = 0
    m = max(priorities)

    while True:
        if m > priorities[0]:
            priorities.append(priorities.pop(0))
            pos.append(pos.pop(0))
        else:
            count += 1
            priorities.pop(0)
            if pos.pop(0):
                return count
            m = max(priorities)