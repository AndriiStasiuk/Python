def task4(num1, num2):
    if (num1 > num2):
        num1, num2 = num2, num1
    x = []
    for i in range(num1, num2 + 1):
        if i > 0:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                x.append(i)
    if x != []:
        print(x)
    else:
        try:
            raise Exception
        except Exception:
            print("Error!!!NoSimpleDigits")
            exit()
