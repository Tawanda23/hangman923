#This task will be using the For Loop to create a pattern using astrix

number = int(input("Please enter a number to begin iteration: ")) #entering a number will start the program up

for row in range(1, 6): #the value 'row' will print rows of stars/astrix. Prints out a maximum of 5 rows
    print("*" * row) #this multiplies the the astrix "*" by the value which is stored in "row" and prints the output