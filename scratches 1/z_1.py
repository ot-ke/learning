# Задачка 1

num1=int(input("Введите число 1: "))
num2=int(input("Введите число 2: "))

print("Сумма:", num1+num2)
print("Произведение:", num1*num2)

if num2 == 0:
    print("Ошибка: второе число равно нулю")
else:
    print("Разность:", num1/num2)

print("Возведение в степень:", num1**num2)

if num2 == 0:
    print("Ошибка: второе число равно нулю")
else:
    print("Целочисленное деление:", num1//num2)

if num2 == 0:
   print("Ошибка: второе число равно нулю")
else:
   print("Остаток от деления:", num1%num2)
