name = input()
letters = []
flag = 0

for i in range(len(name)):
    if name[i] not in letters:
        letters.append(name[i])
if len(letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
