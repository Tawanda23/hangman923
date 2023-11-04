while True:
    user_option = input ("To start a new calculator file, type (y)! To read from a text file, type (n)! : ")
    # Writing a new file section
    #****************************
    if user_option == "y":
        print("You have selected to start a new calculator file!")
        # Handling the ValueError exception using While loop and a Try-Except block
        # Therefore restarting this part of the program, prompting the user to re-enter.
        while True:
            try:
                # Asking users to input two numbers.
                num_1 = int(input("Please enter your first number: "))
                num_2 = int(input("Please enter your second number: "))
                break
            # ValueError exception to notify user that only integers are accepted.
            except ValueError:
                print("Oops! That was not a valid number. Try again!")
                       
        # Asking users to input operation symbol.              
        symbol = input("Please add your operator eg, +, -, *, /: ")

        # Using a if-elif-else statement, program can distinguish the opration required.
        # Addition operator
        if symbol == "+":
            # Using f-string to showcase the entries and followed by the result.
            equation = (f"{num_1} + {num_2} = {int(num_1+num_2)}")
            # Print the answer to equation.
            print(equation)
            # Create a file called "new_equation.txt" and using 'a' to append so that new entries are not overwritten.
            with open("new_equation.txt", 'a') as file:
                # Add variable to the new text file.
                file.write(equation)
                # Here we start a new line in the text file.
                file.write('\n')
        # Subtraction operator
        elif symbol == "-":
            equation = (f"{num_1} - {num_2} = {int(num_1-num_2)}")
            print(equation)
            with open("new_equation.txt", 'a') as file:
                file.write(equation)
                file.write('\n')
        # Multiplication operator
        elif symbol == "*":
            equation = (f"{num_1} * {num_2} = {int(num_1*num_2)}")
            print(equation)
            with open("new_equation.txt", 'a') as file:
                file.write(equation)
                file.write('\n')
        # For the division operator, to avoid ZeroDivionError, we use a try-except to handle error.
        elif symbol == "/":
            try:
                equation = (f"{num_1} / {num_2} = {int(num_1/num_2)}")
                print(equation)
                with open("new_equation.txt", 'a') as file:
                    file.write(equation)
                    file.write('\n')
            except ZeroDivisionError as e:
                print("Error: Cannot divide by zero")
        break
    # Reading a file section
    #*************************
    # Handling the FileNotFoundError exception using While loop and a Try-Except block
    elif user_option == "n":
        print("You have selected to read from a text file!")
        # FileNotFoundError
        while True:
            file_name = input("Please enter the name of the file you want to open: ")
            try:
                contents = ""
                with open(file_name, 'r+') as file:
                # Iterate over the lines
                    for line in file:
                        contents = contents + line
                    print(contents)
                    break

            except FileNotFoundError:
                msg = "Sorry, the file "+ file_name + "does not exist."
                print(msg)
        break
    # For the first if-else statement, the program notifies the error to user
    else:
        print("Select (y) for new calculator file or (n) to read a text file. Please try again!")
        # Here a space was added so there is space between the above else msg and the program restarting msg.
        
        print("")