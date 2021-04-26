num1=int(input("Введите число 1: "))
num2=int(input("Введите число 2: "))

if num1<num2:
    import random
    number=random.randint(num1, num2)
    print(number)
elif num1>num2:
    import random
    number=random.randint(num2, num1)
    print(number)
else:
    print("Ошибка: числа одинаковые, какие числа ты хочешь получить между двумя совпадающими цифрами, алёё")
