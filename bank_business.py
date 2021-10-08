class Account:
    def __init__(self, init_money=0):
        self._balance = init_money

        if init_money < 1:
            raise Exception("0원 no no!")

    def balance(self):
        return self._balance

    def deposit(self, money):
        self._balance += money


    def withdraw(self, money):
        self._balance -= money
