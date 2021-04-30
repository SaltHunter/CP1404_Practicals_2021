"""
CP1404/CP5632 Practical
Color names in a dictionary
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
COLOR_NAMES = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "BEIGE": "#f5f5dc", "BLUEVIOLET": "#8a2be2",
               "BURLYWOOD": "#deb887", "CADETBLUE": "#5f9ea0", "CHOCOLATE": "#d2691e", "CORAL": "#ff7f50",
               "CORNFLOWERBLUE": "#6495ed"}

color = input("Enter color: ").upper()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("The color for,", color, "is unavailable")
    color = input("Enter color: ").upper()