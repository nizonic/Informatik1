#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.
import copy


class Restaurant:

    def __init__(self, name, cuisine_type, is_open = False):
        self.__name = name
        self.__cuisine_type = cuisine_type
        self.__open = is_open
        self.__menu = {}
        self.__sales = 0

    def describe_restaurant(self):
        return f"This is the restaurant {self.__name}, serving {self.__cuisine_type}"

    def open_restaurant(self):
        self.__open = True

    def close_restaurant(self):
        self.__open = False

    def is_open(self):
        return self.__open

    def add_consumption_unit(self, name, price):
        self.__menu[name] = price

    def remove_consumption_unit(self, name):
        self.__menu.pop(name, None)

    def get_menu(self):
        return copy.deepcopy(self.__menu)

    def sell_unit(self, name):
        if not self.__open:
            raise Warning("Restaurant is closed")
        try:
            self.__sales += self.__menu[name]
        except:
            raise Warning("Item not on menu")
    def get_sales(self):
        return self.__sales

