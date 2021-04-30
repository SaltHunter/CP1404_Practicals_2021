#1. when either the denominator or numerator is a letter or a value which is not a number
#2. when the denominator is 0
#3. you can.
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Please input a valid denominator:")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")