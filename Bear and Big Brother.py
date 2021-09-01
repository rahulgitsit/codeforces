weight = list(input().split(" "))
weight = list(map(int,weight))
count = 0

while not(weight[0] > weight[1]):
    weight[0] *= 3
    weight[1] *= 2
    count += 1
print(count)