class Complex:


    def __init__(self, vecshestv_chast, mnim_chast):
        self.vecshestv_chast = vecshestv_chast
        self.mnim_chast = mnim_chast


    def display(self):
        print("I'm okey:", "a =", self.vecshestv_chast,"+", self.mnim_chast, "* j", "- просто вывод комплексного числа")


    def __add__(self, obj):
        return Complex(self.vecshestv_chast + obj.vecshestv_chast , self.mnim_chast + obj.mnim_chast)


    def show(self):
        print(self.vecshestv_chast,"+", self.mnim_chast, "*j")


    def __sub__(self, obj):
        return Complex(self.vecshestv_chast - obj.vecshestv_chast , self.mnim_chast - obj.mnim_chast)


    def show_minus(self):
        print(self.vecshestv_chast,"-","(", self.mnim_chast,")", "*j")

