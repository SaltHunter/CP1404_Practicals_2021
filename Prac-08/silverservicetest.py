"""Function to test the silver service taxis"""

from silverservicetaxi import SilverService


def main():
    """Test silverservicetaxi"""
    taxi = SilverService("Mercedes S500L", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
