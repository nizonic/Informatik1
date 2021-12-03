#!/usr/bin/env python3

from shop import Shop


class ClothingStore(Shop):

    def __init__(self, capital):
        super().__init__(capital)
        self.__clothes = 0

    def procure(self, price_per_unit, units):
        if units > 10:
            return super().procure(0.8*price_per_unit, units)
        return super().procure(price_per_unit, units)

    def add_procured_units(self, units):
        self.__clothes += units

    def get_produced_units(self):
        return self.__clothes

    def set_produced_units(self, units):
        self.__clothes = units

    def get_status(self):
        stats = list(super().get_status())
        stats.append(self.__clothes)
        return tuple(stats)


if __name__ == "__main__":
    c = ClothingStore(10000)
    c.procure(1, 1000)
    print(c.get_status())  # 9200, 0, 0, 0, 1000
    c.sell(5, 1000)
    c.get_status()  # 13200, 0, 0, 0, 0
    c.pay_rent_and_loan(1000)
    c.get_status()  # 12200, 0, 0, 0, 0