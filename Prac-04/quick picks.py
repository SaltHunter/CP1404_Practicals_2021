"""
CP1404/CP5632 Practical - Suggested Solution
Quick pick program
"""

import random

NPL = 6
MIN = 1
MAX = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NPL):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        # the following uses a generator expression (like a list comprehension)
        # to format each number in quick_pick in the same way
        # this is then turned into a single string with the join method
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()