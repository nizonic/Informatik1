#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar:

    def __init__(self, battery_size, battery_range_km):
        self.__c_max = battery_size             #maximum capacity
        self.__range = battery_range_km         #max range with full battery
        self.__c = battery_size                 #current juice left

    def charge(self, kwh):
        if not isinstance(kwh, float): raise Warning
        if kwh < 0: raise Warning
        if self.__c + kwh > self.__c_max:
            raise Warning("Overcharging the battery")
        self.__c += kwh

    def get_battery_status(self):
        return (self.__c, self.__c_max)

    def get_remaining_range(self):
        return self.__range / self.__c_max * self.__c

    def drive(self, dist):
        if not isinstance(dist, float): raise Warning
        if dist < 0: raise Warning
        if dist > self.get_remaining_range():
            self.drive(self.get_remaining_range())
            raise Warning("Battery depleted")
        self.__c -= self.__c_max / self.__range * dist


if __name__ == "__main__":
    e = ElectricCar(25.0, 500.0)
    e.drive(100.0)
    e.charge(2.0)
    print(e.get_battery_status())  # (22.0, 25)