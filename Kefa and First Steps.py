num = int(input())
money = list(input().split(" "))
money = [int(i) for i in money]

prev = -9999999
count = 0
maxVal = 0
for i in money:
    if prev <= i:
        count += 1
    else:
        if maxVal < count:
            maxVal = count
        count = 1
    prev = i

print(max(maxVal, count))