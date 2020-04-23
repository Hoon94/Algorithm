N = int(input())
word_list = list()

for i in range(N):
    word = input()
    count = len(word)
    word_list.append((word, count))

word_list = list(set(word_list))

word_list.sort(key= lambda x: (x[1], x[0]))

for i in word_list:
    print(i[0])