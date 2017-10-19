#!/usr/bin/env python3

#Edit the list easily

def getfile(y):
    y = y.readlines()
    x = []
    for l in y:
        l = l.rstrip('\n')
        x.append(l)
    return x

def printline(y):
    x = getfile(y)
    s = ""
    i = 1
    for l in x:
        l = "Line " + str(i) + ": " + l + '\n'
        s = s + l
        i +=1
    print('\033c' + s)

def editline(a,x):
    x = getfile(x)
    try:
        a = int(a)
    except TypeError:
        print("Function editline: specified incorrect data type!")
        quit()
    if a in range(1,4):
        print("You are trying to edit the decorations!")
    else:
        try:
            a = x[a-1]
        except IndexError:
            print("Function editline: specified incorrect data type!")
            quit()
        print(str(a))
        y = input("> ")
        x[a] = y
        print(x[a])
