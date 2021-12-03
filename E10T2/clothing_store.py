#!/usr/bin/env python3

from shop import Shop


class ClothingStore(Shop):

    def __init__(self, capital):
        super().__init__(capital)

    def procure(self, price_per_unit, units):
        pass

    def add_procured_units(self, units):
        pass

    def get_produced_units(self):
        pass

    def set_produced_units(self, units):
        pass

    def get_status(self):
        pass