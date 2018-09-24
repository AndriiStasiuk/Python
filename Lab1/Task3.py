
def task3(num1, num2):
    if (num1 >= 0 and num2 >= 0):
            if (num1 % num2 == 0):
                return (bool(1))
            else:
                return (bool(0))
    else:
            raise Exception("Ви ввели від'ємне значення!")