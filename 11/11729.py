def hanoi(n : int, a : int, b : int, c : int):
    if n == 1:
        move.append([a, c])
        return None
    
    hanoi(n - 1, a, c, b)
    move.append([a, c])
    hanoi(n - 1, b, a, c)


move = []
hanoi(int(input()), 1, 2, 3)

print(len(move))
for a, b in move:
    print('{} {}'.format(a, b))