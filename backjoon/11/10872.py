def factory(a : int):
    if a == 1 or a == 0:
        return 1
    return a * factory(a - 1)

a = int(input())

print(factory(a))