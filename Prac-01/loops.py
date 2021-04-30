def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for a in range(0, 101, 10):
        print(a, end=' ')
    print()

    for b in range(20, 0, -1):
        print(b, end=' ')
    print()

    stars= int(input("Input your number here:"))
    for s in range(stars):
        print("*", end = '  ')

    stars = int(input("Input your number here:"))
    for s in range(0, stars):
        for x in range(0, s + 1):
            print("*", end='  ')
        print()
main()