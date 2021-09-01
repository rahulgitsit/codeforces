n = input()
cubes = list(input().split(" "))
cubes = list(map(int, cubes))
cubes.sort()
[print(i, end=" ") for i in cubes]
