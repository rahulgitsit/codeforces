num = list(input().split(" "))
num = [int(i) for i in num]
bananaCost = 0

for i in range(1,num[2]+1):
    bananaCost += i * num[0]

if num[1] > bananaCost:
    print(0)
else:
    print(bananaCost - num[1])