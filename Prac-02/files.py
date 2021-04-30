def main():
    namelist = open("namelist.txt", "w")
    x = str(input("Please input your name here:"))
    file.write(namelist)
    namelist.close()

    namelist = open("namelist.txt", "r")
    namelist = fle.read().strip()
    print("Your name is", x)
    namelist.close()


main()