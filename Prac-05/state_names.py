"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

state = input("Enter short state: PRINT to print all ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    elif state == "PRINT":
        for k, v in STATE_NAMES.items():
            print(k, "is", v)
        print(STATE_NAMES)
    else:
        print("Invalid short state")
    state = input("Enter short state: PRINT to print all ").upper()
