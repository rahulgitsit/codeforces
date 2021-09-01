twinA = 0
amount = 0
count = 0

num = int(input())
coins = input().split(" ")
coins = list(map(int, coins))
coins.sort(reverse=True)

for i in coins:
    amount += i

for i in coins:
    if twinA > amount:
        break
    twinA += i
    amount -= i
    count += 1

print(count)
