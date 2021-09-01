words = []
num = int(input())

for i in range(0, num):
    word = str(input())
    words.append(word)

for i in range(0, num):
    if len(words[i]) > 10:
        words[i] = words[i][0] + str(len(words[i]) - 2) + words[i][-1]
    print(words[i])
