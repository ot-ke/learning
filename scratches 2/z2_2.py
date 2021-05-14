# Написать метод машины под названием describe. Метод печатает строку вида "название машины - цвет машины"


class Car:
#    color = 1
#    name = 2


    def __init__(self, name, color):
        self.name = name
        self.color = color


    def describe(self):
        print("Название машины: ", self.name, " ", "Цвет машины: ", self.color)


car1 = Car("KAMAZ", "Blue-Red-White")
car1.describe()

car2 = Car("UAZ", "Pink")
car2.describe()