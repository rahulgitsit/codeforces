size = input().split(" ")
size = [int(i) for i in size]

boardSize = size[0]*size[1]

dom = int(boardSize // 2)

print(dom)