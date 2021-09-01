def test(num):
    if num % 2 == 0 and num >2:
        print("YES")
    else:
        print("NO")


for i in range(1, 100):
    print(i)
    test(i)
