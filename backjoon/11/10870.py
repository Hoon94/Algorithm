def fibonacci(a : int):
    if a < 2:
        return a
    return fibonacci(a-1) + fibonacci(a-2)

a = int(input())

print(fibonacci(a))