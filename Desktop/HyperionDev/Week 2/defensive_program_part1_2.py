#variables definition

#operators variable that will be used if the if statement
operator = ("/", "+", "-", "*") 

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
    return num1 / num2

#Function to execute file read and Try-Except block to check the file is found
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                num1, operator, num2 = line.split()
                num1 = float(num1)
                num2 = float(num2)
                   
                if operator == "/":
                    result = division(num1, num2)
                    
                elif operator == "+":
                    result = addition(num1, num2)
    
                elif operator == "-":
                    result = subtract(num1, num2)

                elif operator == "*":
                    result = multiply(num1, num2)

                else:
                    print("Entry not Recognised\n")
                    continue
                print(f"{num1} {operator} {num2} = {result}")

    except FileNotFoundError:
        print("File has not been found")

        filename = input("Please enter an appropriate filename: ")
        read_file(filename)

 #Function to define the user number input
def user_number_input():

    operator = input("Enter an operator(/ + - *): ")
    num1 = float(input("Enter number: "))
    num2 = float(input("Enter a number: "))

    if operator == "/":
        result = division(num1, num2)

    elif operator == "+":
        result = addition(num1, num2)
    
    elif operator == "-":
        result = subtract(num1, num2)

    elif operator == "*":
        result = multiply(num1, num2)

    else:
        print("Entry not Recognised\n")
        return
    print(f"{num1} {operator} {num2} = {result} ")


 #Function to define the program run
def program_run():
    print("Please make a selection to proceed: ")
    print("1: Enter two numbers and an operator")
    print("2: Read file to obtain equations")

    #Ask user to choose whether to use two inputs  or to read file
    selection = input("Please enter 1 or 2 to proceed: \n ")

    if selection == "1":
        user_number_input()

    elif selection == "2" :
        filename = input("Please enter a valid name: ")
        read_file(filename)
    else:
        print("Please enter a valid option!")

 
if __name__ == "__main__":
    program_run()

