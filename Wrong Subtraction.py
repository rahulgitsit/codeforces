num = list(input().split(" "))
num = list(map(int, num))

for i in range(0, num[1]):
    if num[0] % 10 != 0:
        num[0] -= 1
    else:
        num[0] /= 10

print(int(num[0]))
