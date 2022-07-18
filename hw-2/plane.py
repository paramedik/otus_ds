"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, additional_cargo: int):
        new_cargo = self.cargo + additional_cargo
        if new_cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo = new_cargo

    def remove_all_cargo(self) -> int:
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
