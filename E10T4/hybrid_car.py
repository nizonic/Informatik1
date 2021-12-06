#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__mode = True     #True for electrical mode, False for combustion mode

    def switch_to_combustion(self):
        self.__mode = False

    def switch_to_electric(self):
        self.__mode = True

    def get_remaining_range(self):
        return ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)

    def drive(self, dist):
        if not isinstance(dist, float): raise Warning
        if dist < 0: raise Warning
        c_range = CombustionCar.get_remaining_range(self)
        e_range = ElectricCar.get_remaining_range(self)
        if dist > self.get_remaining_range():
            CombustionCar.drive(self, c_range)
            ElectricCar.drive(self, e_range)
            raise Warning("out of juice")
        if self.__mode:
            if dist >= e_range:
                ElectricCar.drive(self, e_range)
                self.switch_to_combustion()
                CombustionCar.drive(self, dist - e_range)
            else: ElectricCar.drive(self, dist)

        else:
            if dist >= c_range:
                CombustionCar.drive(self, c_range)
                self.switch_to_electric()
                ElectricCar.drive(self, dist - c_range)
            else: CombustionCar.drive(self, dist)



if __name__ == "__main__":
    h = HybridCar(40.0, 8.0, 25.0, 500.0)
    h.switch_to_combustion()
    h.drive(600.0)  # depletes fuel, auto-switch
    h.get_gas_tank_status()  # (0.0, 40.0)
    h.get_battery_status()
    h.drive(500.0)# (20.0, 25.0)