N = int(input())
member = list()
count = 0

for i in range(N):
    age, name = input().split()
    count += 1
    member.append((count, int(age), name))

member.sort(key= lambda x : (x[1], x[0]))

for i in member:
    print(i[1], i[2])