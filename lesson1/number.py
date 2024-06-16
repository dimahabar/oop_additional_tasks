"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""



class Number:


    def __init__(self, val: int):
        self.val = val

    def get(self):
        return self.val


    def add(self, amount):
        self.val += amount
        return amount



    def substract(self, add):
        self.val -= add
        return add


# код для проверки 
x = Number(7)
print(x.get())  # 7
x.add(3)
print(x.get())  # 10
x.substract(5)
print(x.get())  # 5
