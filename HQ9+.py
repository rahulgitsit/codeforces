p = list(input())
flag = 0

for i in p:
    if i in ['H','Q','9']:
        print("YES")
        flag = 1
        break
if flag == 0:
    print("NO")