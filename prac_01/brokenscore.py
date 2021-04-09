"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!
# If the score is bigger than 100 or score is less than 0 then it is invalid score(Error)
# Else Determine wether score is good or bad

def main():


    score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score > 90:
        print("Excellent")

    elif score >= 50:
        print("Passable")

    else:
        print("Bad")
main()
