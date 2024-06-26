"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    balance: float


    def __init__(self, balance):
        self.balance = balance


    def balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return amount

    # Используйте условие if, чтобы проверить, имеется ли на счете достаточная
    # сумма денег для обработки вывода средств

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("\n Insufficient balance  ")
    def close(self):
        return self.withdraw(self.balance)



# код для проверки 
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
