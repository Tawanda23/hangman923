
#operators variable that will be used if the if statement
ops = ("/", "+", "-", "*") 

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
    try:
        return num1 / num2
    except ZeroDivisionError:
        return("Can't divide by zero")

#EQUATION TO WRITE TO FILE
def writing_to_file(num1, num2, operator, result):
    with open("cal_equation.txt", "a") as file:
        file.write(f"{num1} {operator} {num2} = {result} /n")

#EQUATION TO PERFORM CALCULATIONS
def calculation(num1, num2, operator):
    if operator == "/":
        result = division(num1/num2)
    elif operator == "+":
        result = addition(num1+num2)
    elif operator == "-":
        result = subtract(num1-num2)
    elif operator == "*":
        result = multiply(num1*num2)
    else:
        result = "Invalid Operator Entry"
        print(f"{num1} {operator} {num2} = {result}") #double check

def main_calculation():
    while True:
        try:
            print("\n")
            print("Please make a selection from the selections below to proceed: \n")
            print(" '1' to Enter two numbers and an operator or '2' To Read file to obtain equations: \n ")
           
            selection = input("Please enter 1 or 2 to proceed: \n")

            if selection == "1":

                num1 = float(input("1: Enter a number"))
                num2 = float(input("1: Enter a number"))
                operator = input("enter operator: \n ") 
                result = calculation(operator, num1, num2)
                print(f"{num1} {operator} {num2} = {result}")
                writing_to_file(operator, num1, num2, result)

            elif selection == "2" :
                filename = input("Please enter a valid name: ")
                with open(filename, 'r') as file:
                    for line in file:
                        num1, operator, num2 = line.split()
                        num1 = float(num1)
                        num2 = float(num2)
                        operator = input("enter operator ("/", "+", "-", "*")") 
                        result = calculation(operator, num1, num2)
                        print(f"{num1} {operator} {num2} = {result}")
                    else:
                        print("File not found")
            else:
                print("Error: Invalid input")

        except ValueError:
            print("Error: Invalid input. Please enter a number.")

        except ZeroDivisionError:
            print("Error: Division by zero")
if __name__ == "__main__":
    main_calculation()

 