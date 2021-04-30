"""CP1404 Taxi Simulator"""
from car import Car
from taxi import Taxi
from silverservicetaxi import SilverService

menu = "(q)uit, (c)hoose taxi, (d)rive"


def main():
    """
    Write a taxi simulator code which uses the taxi and silverservice classes.
    Each time untill the user quits:
    1. The user should be presented with a list of available taxis to get and choose one.
    2. The user would then state how far they would want to drive it.
    3. At the end of the user's trip, show the price and add it to their bill
    """

    bill = 0
    taxis = [
        Taxi("Prius", 100),
        Taxi("Camry", 150),
        SilverService("Mercedes S500L", 200, 4),
        SilverService("Tesla Model S", 200, 6)
    ]

    print("Let's Drive")
    print(menu)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            # no error-checking
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                         trip_cost))
            bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill))
        print(menu)
        menu_choice = input(">>> ").lower()

    print("Total Trip Cost: ${:2f}".format(bill))
    print(menu)
    menu_choice = input(">>> ").lower()


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def cartest():
    """Function to test the car and taxi classes"""
    car = Car("Mazda RX-7 Infini-3", 50)
    car.drive(10)
    print("fuel = ", car.fuel)
    print("odo = ", car.odometer)
    car.drive(20)
    print("fuel = ", car.fuel)
    print("odo = ", car.odometer)
    print(car)

    # drive car
    distance = int(input("Drive how far"))
    while distance > 0:
        travelled = car.drive(distance)
        print("{} travelled {}".format(str(car), travelled))
        distance = int(input("Drive how far?"))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverService("Mercedes S500L", 200, 4)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


main()
