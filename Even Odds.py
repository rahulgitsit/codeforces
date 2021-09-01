import math

n = input().split(" ")
n = list(map(int, n))
mid = math.ceil(n[0]/2)
if n[1] <= mid:
    print(2*n[1]-1)
else:
    print(2*(n[1]-mid))
