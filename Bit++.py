n = int(input())
x = 0
statement = []
for i in range(0, n):
    statement.append(input())
    if "++" in statement[i]:
        x += 1
    elif "--" in statement[i]:
        x -= 1

print(x)
