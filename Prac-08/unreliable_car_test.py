"""
CP1404 Practical Unreliable Car test
An unreliable car would not always drive
These tests will verify wether a car is reliable or not
We expect a more reliable car to drive more often than an unreliable car
"""

from unreliable_car import UnreliableCar


def main():
    """Function to test the reliability of a car"""

    # Create cars with diffrent reliabilities
    Reliable_car = UnreliableCar("Mostly Good", 100, 90)
    Unreliable_car = UnreliableCar("Dodgy", 100, 9)

    # Multiple drives of the car attempted to test its reliability
    # output the distance they drove
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(Reliable_car.name, Reliable_car.drive(i)))
        print("{:12} drove {:2}km".format(Unreliable_car.name, Unreliable_car.drive(i)))

    # Print Final car state
    print(Reliable_car)
    print(Unreliable_car)


if __name__ == '__main__':
    main()
