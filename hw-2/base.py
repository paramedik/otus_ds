from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: int, fuel: int, fuel_consumption: int):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance: int):
        fuel_consumption_for_distance = self.fuel_consumption * distance
        if self.fuel < fuel_consumption_for_distance:
            raise NotEnoughFuel
        else:
            self.fuel -= fuel_consumption_for_distance

