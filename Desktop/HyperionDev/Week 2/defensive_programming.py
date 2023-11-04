#the functions are defined  here before the program starts

#Function to execute addition
def addition(num1,num2):
    return(num1 + num2)

#Function to execute subtraction
def subtract(num1,num2):
    return(num1 - num2)

#Function to execute multiplication
def multiply(num1,num2):
    return(num1 * num2)

#Function to execute division
def division(num1,num2):
    try: #here, the 'try' block is used to raise an exception so that the code is fool proof
        return num1 / num2
    except ZeroDivisionError: #this exception is for when the user divides by 0. It will print out the statement below
        return("Can't divide by zero")

while True:
    print(" \n Please make a selection below to proceed: \n ") #this will start the program. User will be asked to make a selection to start the calculator
    print("1: To start a new file, Enter two numbers and an operator") #user option to input two numbers and an operator
    print("2: Read file to obtain equations") #user option to read file to get equations

    #Ask user to choose whether to use two inputs  or to read file
    selection = int(input("Please enter 1 or 2 to proceed: \n ")) # in this part of the code, the user input has been set to be an integer so that we are not adding intergers to strings

    if selection == 1: #the code will start running here if the user selects option 1 which uses two numbers and an operator
        print("\n You have selected to start a new file. Lets get started! \n") #This lets the user know that their calculations will be starting
        print("File name: \n new_calculation_equation.txt \n")    

        while True: # while loop is used to raise an exception to ensure only numerical numers are used
            try:
                operator = input("Enter an operator(/ + - *): ") #user inputs an operator
                num1 = float(input("Enter number: ")) #user inputs num1 as a float
                num2 = float(input("Enter a number: ")) #user inputs num2 as a float
                break
            except ValueError: #value error is raise if anything other than an integer/float is used
                print("Please Enter numerical figures")


        if  operator == "/": #division operator
            result = division(num1, num2)
            calc_result = (f"{num1} {operator} {num2} = {result} ") #prints out the result as an f-string
            print(calc_result) #the result of the calculation will be calculated here
            with open("new_calculation_equation.txt", 'a') as file: #opens the file 'new_calculation_equation' if it exists. The 'a' is for appending
                file.write(calc_result) #this writes the result to the file as string
                file.write('\n') #adds a new line to the print in the txt file

        elif operator == "+": #addition operator
            result = addition(num1, num2)
            calc_result = (f"{num1} {operator} {num2} = {result} ") #prints out the result as an f-string
            print(calc_result) #the result of the calculation will be calculated here
            with open("new_calculation_equation.txt", 'a') as file: #opens the file 'new_calculation_equation' if it exists. The 'a' is for appending
                file.write(calc_result) #this writes the result to the file as string
                file.write('\n') #adds a new line to the print in the txt file

        elif operator == "-": #subtraction operator
            result = subtract(num1, num2)
            calc_result = (f"{num1} {operator} {num2} = {result} ") #prints out the result as an f-string
            print(calc_result) #the result of the calculation will be calculated here
            with open("new_calculation_equation.txt", 'a') as file: #opens the file 'new_calculation_equation' if it exists. The 'a' is for appending
                file.write(calc_result) #this writes the result to the file as string
                file.write('\n') #adds a new line to the print in the txt file

 
        elif operator == "*": #multiplication operator
            result = multiply(num1, num2)
            calc_result = (f"{num1} {operator} {num2} = {result} ") #prints out the result as an f-string
            print(calc_result) #the result of the calculation will be calculated here
            with open("new_calculation_equation.txt", 'a') as file: #opens the file 'new_calculation_equation' if it exists. The 'a' is for appending
                file.write(calc_result) #this writes the result to the file as string
                file.write('\n') #adds a new line to the print in the txt file      
        break

        #Reading a file
    elif selection == 2: #the user has chosen option 2 which will ask them to choose a filename

        print("\n You have selected to readfrom a file. Lets get started! \n") #This lets the user know that their calculations will be starting
        print("File name:\n new_calculation_equation.txt \n") 

        while True:
            filename = input("Please enter the file name: ") #asks user to input an appropriate file name
            try:
                file_contents = "" #this is an empyt variable that will be used to store contents of the file once opened
                with open(filename, 'r+') as file: #this will aim to open the file that user will have specifies. The 'r' states that the file is for reading. This 'with' block also ensures that the code block closes once code has been run inside the block
                    for line in file: #this reads the contents of the file line by line
                        file_contents = file_contents + line #here, the contents of the file are linked with the all the lines that have been read
                    print(file_contents) #this prints out all the equations that have been to written to the file
                    break
            except: FileNotFoundError #will execute this except if the program fails to read the file as expected
            print("The file you are looking for does not exist")

        break #this will break the loop once the conditions of While True are met
    else:
            print("Please Try Again") #user is told to try again