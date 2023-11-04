#variables definition

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

#This will open a file called: calculation_output
file = open("cal_equation.txt", 'a')

while True: #if all the 3 variables are correct, the while loop will start running
    try:
        operator = input("Enter an operator(/ + - *): ")
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter a number: "))

        cal_equation = (str(num1)+" "+operator+" "+str(num2))

    except ValueError:

        file.write(cal_equation+"\n")

    if operator in ops:

        if operator == "/":
            print(division(num1, num2))

        elif operator == "+":
            print(addition(num1, num2))
    
        elif operator == "-":
            print(subtract(num1, num2))

        elif operator == "*":
            print(multiply(num1, num2))

        print(cal_equation)

    else:
        print("Invalid Operator Entry")

    file.close()





#the nect section will be trying to read the contents of the file that we are looking at 
try:
    file2 = open("calculation_output.txt", 'r')
    print(file2.read())
    file2.close
except IOError:
    file2.close()