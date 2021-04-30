"""CP1404 Silver Service Taxis Function"""
from taxi import Taxi


class SilverService(Taxi):
    """Specialized taxi which has a diffrent effective price per km"""
    Flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize a silver service taxi"""
        super(SilverService, self).__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of Silver Service Taxis"""
        return "{} plus flagfall of ${:2f}".format(super().__str__(), self.Flagfall)

    def getfare(self):
        """Get the current fare"""
        return self.flagfall + super().getfare()
