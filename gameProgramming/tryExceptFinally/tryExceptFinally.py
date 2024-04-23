# Method for testing code and preventing crashes.
# try -- except -- else -- finally

try: # Code in this block is always executed.
    myVariable = 1
    print(myVariabl)
except NameError: # Code will run if there is an error (exception)
    print("There is an incorrect variable name in your code.")
except:
    print("Something has gone wrong.")
else:
    print("Code executed correctly with no exceptions.")
finally:
    print("I'll be back.")