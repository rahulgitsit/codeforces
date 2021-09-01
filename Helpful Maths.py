finalSum = ""
xeniaSum = []

xeniaSum = str(input()).split("+")
xeniaSum.sort()
for i in xeniaSum[:-1]:
    finalSum += i + "+"

finalSum += xeniaSum[-1]

print(finalSum)

