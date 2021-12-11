#!/usr/bin/env python3
# add imports, if necessary
from exchange_rates import EXCHANGE_RATES
from currency_converter import convert

class BankAccount:

    def __init__(self, currency="CHF"):
        if currency not in EXCHANGE_RATES:
            raise Warning("Currency not available")
        self.__currency = currency
        self.__balance = 0

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance

    def deposit(self, amount, currency="CHF"):
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise Warning("Not a number")
        if amount < 0:
            raise Warning("Cannot deposit a negative amount")
        if currency not in EXCHANGE_RATES:
            raise Warning("Currency not available")
        self.__balance += convert(amount, currency, self.__currency)
    def withdraw(self, amount, currency="CHF"):
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise Warning("Not a number")
        if amount < 0:
            raise Warning("Cannot withdraw a negative amount")
        if currency not in EXCHANGE_RATES:
            raise Warning("Currency not available")
        if convert(amount, currency, self.__currency) > self.__balance:
            raise Warning("Can't withdraw amount greater than balance")
        self.__balance -= convert(amount, currency, self.__currency)



if __name__ == "__main__":
    sut = BankAccount("CHF")
    sut.deposit(100.0, "CHF")
    sut.withdraw(10.0, "EUR")
    print(sut.get_balance())
    expected = 89.0