line1 = input()
line2 = input()

if str.lower(line1) == str.lower(line2):
    print(0)
elif str.lower(line1) > str.lower(line2):
    print(1)
else:
    print(-1)