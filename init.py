#!/usr/bin/env python3

#Welcome to list!
print("\033clist")
print("(C) 2017 Saksham Mittal")

print("")
x = input("Name of file: ")

#Gets all of the command line arguments in case the user wants to edit the file
import sys
flags = sys.argv[1:]

#If there are any flags, execute the corresponding functions
try:
    if flags[0] == "edit":
        try:
            y = open(x)
        except:
            print("An error occured!")
            quit()
        import edit
        edit.printline(y)
        print("Which line would you like to edit?")
        x = input("> ")
        try:
            x = int(x)
        except TypeError:
            print("An error occured!")
            quit()
        edit.editline(x,y)

#If not, make a new list
except IndexError:
    #If the file exists, quit, else, make the file
    try:
        y = open(x,"x")
        y.close()
    except FileExistsError:
        print("This file already exists!")
        quit()

    y = open(x,"a")
    
    #Now, let's get started with the actual list making
    import functions
    functions.main(1,y)
