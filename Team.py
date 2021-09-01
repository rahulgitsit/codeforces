sol = []
count=0
num = int(input())

for i in range(0, num):
    sol.append(str(input()))
    if sol[i] in ['1 1 1', '1 1 0', '1 0 1', '0 1 1']:
        count += 1

print(count)