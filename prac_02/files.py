def main():


# 1. Write code that asks for the user names, and opens a file called name.txt, and writes the name onto it
# 2. Write code that opens "name.txt" and reads the name as above and then prints "Your name is USERNAME"
# 3. Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 5
# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.

    namelist = open("name.txt", 'w')
    nameinput = str(input("Please input Your Name Here. . ."))
    namelist.write(nameinput)
    namelist.close()

    nameread = open("name.txt", 'r')
    name = nameread.read().strip()
    print("Your Name Is", name)
main()
