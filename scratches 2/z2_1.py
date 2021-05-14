# Написать класс машины (Car). Имеет поля цвет(color), марку(name). Переменные принимаются в конструктор. Например, car1 = Car("red", "audi")

class Car:
    color = 1
    name = 2


    def __init__(self, name, color):
        self.name = name
        self.color = color


    def display_info(self):
        print("Марка автомобиля: ", self.name, " ", "Цвет автомобиля: ", self.color)


car1 = Car("KAMAZ", "Blue-Red-White")
car1.display_info()

car2 = Car("UAZ", "Pink")
car2.display_info()