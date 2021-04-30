"""CP1404 Unreliable Car class"""

from random import randint
from car import Car


class UnreliableCar(Car):
    """The unreliable version of a car"""

    def __init__(self, name, fuel, reliability):
        """Initialize an unreliable car"""
        super(UnreliableCar, self).__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Sometimes Drive the car, depending on reliability"""
        number = randint(1, 100)
        if number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
