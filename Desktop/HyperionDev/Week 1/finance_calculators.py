import math #use the import math function to allow the program to use mathematical functions to perform calculations

#Investmet - to calculate the amount of interest you will earn on your investment #Bond - to calculate the amount of interest you will have to pay back on a home loan

print("\nInvestment - calculates the amount of interest you will earn on your investment", "\n" "Bond - calculates the amount of interest you will have to pay on a home loan \n")

#=================================Investment Choice==============================

#Calculatorn choice - this will allow  the  user to choose which calcuator they wish to use
calculator_choice = input("Enter either 'investment' or 'bond':\n ").lower() #this will ask the user to choose if they want an investment calculator or if they want a bond calculator. This is case insensitive and will not matter how the user inputs the choice

if calculator_choice == 'investment':
    deposit = 0 #deposit that the user will input
    rate = 0 #this is the rate of interest charged
    time = 0 #this is the time period that the user will be investing for
    simple_interest = (deposit * (1 + rate * time)) #simple interest calculation formula

    deposit = float(input("Enter deposit amount: ")) # caluclator will be able to process decimal numbers
    
    if deposit <= 0:
        print("Deposit amount can't be less than zero")
    else:
        rate = float(input("Enter interest rate: ")) #caluclator will be able to process decimal numbers
        if rate <= 0:
            print("Interest rate can't be less than zero") #this block is initiated if the user enters a rate of zero
        else:
            time = int(input("Enter time in years: ")) # caluclator will only be able to process integers
            if time < 0:
                print("Time can't be less than or equal to zero") #this block is initiated if the user enters zero for the time they want to invest for

            else:
                #printing out the user inputs
                print("£",deposit)
                print(rate,"%")
                print(time, "years")
                
                print("Do you want 'Simple' or 'Compound interest'?") #program asks the user the type of interest they want to calculate

                interest_type = input("Please enter interest type:\n simple\n compound\n ") #user input for the type of interest they want to calculate

    #user will be able to the choose type of interest that tthey want to be calculated
                #simple interest option
                if interest_type == "simple": #this IF statement will execute if the user chooses 'simple' interest
                    print("You have chosen Simple interest")
                    total = deposit*(1 + (rate/100) * time) #formula to calculate total simple interest

                #compound interest option
                elif interest_type == "compound": #this IF statement will execute if the user chooses 'compound' interest
                    print("You have chosen compound interest")
                    total = deposit * pow(1 + (rate/100),time)#formula to calculate total 'compound' interest

                else:
                    print("invalid request!") #this prints out a statement if the user enters anything other than 'simple' or 'compound'
                print(f"Balance after {time} years: £{total:.2f}") #the final amount will be formatted to 2 significant figures

    #=================================Bond Choice==============================
else:
    if calculator_choice == 'bond':

        #Variables for Bond Repayment
        house_value = 0 #this is the house value that the user will have input
        bond_rate = 0 #this is the rate of interest charged charged on the bond
        time = 0 #this is the bond repayment time

        house_value = float(input("Enter house value: "))#calculator will be able to process decimal numbers for house value

        if house_value < 0:
            print("House value can't be less than zero")
        else:
            bond_rate = float(input("Enter interest rate: "))#calculator will be able to process decimal numbers for bond rate
            if bond_rate < 0:
                print("Interest rate can't be less than zero")
            else:
                time = int(input("Enter time in months: "))# caluclator will only be able to process integers (whole number)
                if time < 0:
                    print("Time can't be less than or equal to zero")
                else:
                    bond_interest = ((bond_rate/100)/12)
                    #printing out the user inputs
                    print("£",house_value)
                    print(bond_rate,"%")
                    print(time, "months")
                    print(bond_interest)

    #repayment rate calculated to be paid per month
                    repayment = (bond_interest * house_value)/(1-(1 + bond_interest) ** (-time))
                    print(f"Total monthly bont repayment: £{repayment:.2f}") #the final amount will be formatted to 2 significant figures

    else:
        print("Invalid Value Entry ") #Error message to alert user if they have entered anything outside of 'investment' or 'bond'

 