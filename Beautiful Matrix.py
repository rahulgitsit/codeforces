import math

matrix = []
row = 0
col = 0

for i in range(0, 5):
    matrix.append((input()))
    if '1' in matrix[i]:
        row = i

matrix = matrix[row].split(" ")

col = matrix.index('1')

print(abs(row - 2) + abs(col - 2))
