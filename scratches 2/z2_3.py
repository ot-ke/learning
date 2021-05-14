# Написать класс для комплексного числа Complex. Принимает в конструктор целую и вещественную части, напримеp для числа a=2+3j будет написано
# a=Complex(2,3).
# Переопределить операторы сложения и вычитания.

from z2_3_classes import Complex

a=Complex(7,15)
a.display()

f1=Complex(12,36)
f2=Complex(5,35)

print("Первое складываемое число:")
f1.show()
print("Второе складываемое число:")
f2.show()

result = f1 + f2
print("Результат сложения:")
result.show()

result_minus = f1 - f2
print("")
result_minus.show_minus()