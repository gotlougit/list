#!/usr/bin/env python3

#The main interface that is supposed to be executed by users
#WARNING: DO NOT MODIFY list TO NOT USE THIS SETUP!
#list tries to be as user-friendly as possible


#Provides a finishing UNIX feel to list
try:
    import init
except KeyboardInterrupt: #Use Ctrl-C freely!
    print("\n")
    quit()
except EOFError: #Use Ctrl-D freely!
    print("")
    quit()
