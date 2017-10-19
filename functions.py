#!/usr/bin/env python3

#The functions necessary for making a list

#What to do when the user wants to end the list
def pointsend():
    print("\033cDONE!")
    quit()

#What to do when the user ends the subpoints
def subsend(n,f,ls):
    i = ""
    for l in ls:
        i = i + l
    print("\033c" + i)
    points(n+1,f,ls)

#Makes a nice little border and decorates the title.
#Not your run-of-the-mill list program, is it?
def title(ls,f):
    x = input("Title: ") #Ask the title
    i = 0
    for c in x:
        i+=1
    i+=1
    #the above code finds out how many characters are in the title
    y = "-"*2*i 
    # Generates a horizontal line that is twice the length of the title + 1
    ls.append(y+'\n') 
    ls.append(x+'\n')
    ls.append(y+'\n') #Add the title to the internal list object 
    f.write(y + '\n')
    f.write(x + '\n')
    f.write(y + '\n') #Write the title to the file
    print('\033c'+ y) #Clear screen and print the result!
    print(x)
    print(y)

#Function to get the information necessary to write the main stuff in the list 
def points(n,f,ls):
    x = str(n) + ". " #Helps to make an ordered list
    y = input(x)
    if y == "":
        pointsend() #If the user presses enter, end the points
    else:
        x = x + y 
        ls.append(x + '\n') #Add x to the internal list object
        x = f.write(x + '\n') #Write x to the file
        subs(n,f,ls) #Subpoints

#If they want, the user can add subpoints, the functionality is all here
def subs(n,f,ls):
    x = '\t* ' #Adds a bullet point
    y = input(x)
    if y == "":
        subsend(n,f,ls) #If the user presses enter, end the subpoints
    else:
        x = x + y
        ls.append(x + '\n') #Add x to the internal list object
        x = f.write(x + '\n') #Write x to the file
        subs(n,f,ls) #Add more subpoints

#The main function that is executed by init.py
def main(n,f):
    ls = [] #Make a brand new list object
    try:
        title(ls,f) #Get the title
        points(n,f,ls) #Make points
    except: #Catch all exceptions and at least close the program cleanly
        quit()
