num = list(map(int, input().split()))
puzzles = list(map(int, input().split()))
puzzles.sort()

maxDiff = 9999999

if num[0] == num[1]:
    print(max(puzzles) - min(puzzles))
else:
    for i in puzzles:
        for j in puzzles[1:]:
            if