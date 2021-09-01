n = input().split(" ")
k = [int(i) for i in n]
n = k[0]
k = k[-1]

print(n, k)
count = 0
scores = input().split(" ")
mapList = list(map(int, scores))
print(mapList)

for i in range(0, n):
    if mapList[i] >= mapList[k-1] and mapList[i] != 0:
        count += 1
    else:
        break

print(count)
