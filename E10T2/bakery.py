#!/usr/bin/env python3

from shop import Shop


class Bakery(Shop):

    def __init__(self, capital):
        super().__init__(capital)
        self.__bread = 0
        self.__dough = 0

    def sell(self, price_per_unit, units):
        return super().sell(0.75*price_per_unit, units)

    def produce(self, costs_per_unit):
        while self.__dough > 0 and self._capital >= costs_per_unit:
            self.__bread += 1
            self.__dough -= 1
            self._capital -= costs_per_unit
            if self._capital < costs_per_unit:
                raise Warning("not enough capital")

    def procure(self, price_per_unit, units: int):
        return super().procure(price_per_unit, units)

    def add_procured_units(self, units):
        self.__dough += units

    def get_produced_units(self):
        return self.__bread

    def set_produced_units(self, units):
        self.__bread = units

    def pay_rent_and_loan(self, rent):
        return super().pay_rent_and_loan(0.8*rent)

    def get_status(self):
        stats = list(super().get_status())
        stats.extend([self.__dough, self.__bread])
        return tuple(stats)


if __name__ == "__main__":
    b = Bakery(10000)
    b.procure(1, 1000)
    print(b.get_status())  # 9000, 0, 0, 0, 1000, 0
    b.produce(1)
    b.get_status()  # 8000, 0, 0, 0, 0, 1000
    b.sell(4, 1000)
    b.get_status()  # 11000, 0, 0, 0, 0, 0
    b.pay_rent_and_loan(1000)
    b.get_status()  # 10200, 0, 0, 0, 0, 0
    bakery = Bakery(1000)
    bakery.take_loan(0.1, 1000)
    actual = bakery.pay_rent_and_loan(100)
    print(actual)