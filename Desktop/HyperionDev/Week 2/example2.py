import os.path

def write_equation_to_file(num1, num2, operator, result):
    with open("equations.txt", "a") as file:
        file.write(f"{num1} {operator} {num2} = {result}\n")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

def perform_calculation(num1, num2, operator):
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "x":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = "Error: Invalid operator"
    return result

def main():
    while True:
        try:
            choice = input("Enter '1' to perform a calculation or '2' to read from a file: ")
            if choice == "1":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                operator = input("Enter the operator (+, -, x, /): ")
                result = perform_calculation(num1, num2, operator)
                print(f"{num1} {operator} {num2} = {result}")
                write_equation_to_file(num1, num2, operator, result)
            elif choice == "2":
                file_name = input("Enter the name of the file: ")
                if os.path.isfile(file_name):
                    with open(file_name, "r") as file:
                        equations = file.readlines()
                        for equation in equations:
                            equation_parts = equation.split(" ")
                            num1 = float(equation_parts[0])
                            num2 = float(equation_parts[2])
                            operator = equation_parts[1]
                            result = perform_calculation(num1, num2, operator)
                            print(f"{equation.strip()} = {result}")
                else:
                    print("Error: File not found")
            else:
                print("Error: Invalid input")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
        except ZeroDivisionError:
            print("Error: Division by zero")

if __name__ == "__main__":
    main()

