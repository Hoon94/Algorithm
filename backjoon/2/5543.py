a = input()
b = input()
c = input()
d = input()
e = input()

cheap = 4000
burger = [int(a), int(b), int(c)]
beverage = [int(d), int(e)]

for i in range(len(burger)):
    for j in range(len(beverage)):
        total = burger[i]+beverage[j] - 50
        if total < cheap :
            cheap = total

print(cheap)