balance = input()

num1 = int(balance[:-1])
num2 = int(balance[:-2] + balance[-1])

if '-' in balance:
    if num1 > num2:
        print(num1)
    else:
        print(num2)
else:
    print(balance)