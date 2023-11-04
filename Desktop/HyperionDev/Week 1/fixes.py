import math

#Investmet - to calculate the amount of nterest you will earn on your investment
#Bond - to calculate the amount of interest you will have to pay on a home loan

print("Investmet - to calculate the amount of nterest you will earn on your investment", "\n" "Bond - to calculate the amount of interest you will have to pay on a home loan")

#Calculatorn choice
calculator_choice = input(str("Enter either 'investment' or 'bond':\n ").lower())
"\n"
if calculator_choice == 'investment':
    
    #variables 
    principle = 0
    rate = 0
    time = 0
    simple_interest = (principle * (1 + rate * time))

    principle = float(input("Enter deposit amount: "))
    rate = float(input("Enter interest rate: "))      
    time = int(input("Enter time in years: "))

    # printing outputs       
    print("£",principle)
    print(rate,"%")
    print(time, "years")

    print("Do you want Simple or Compound interest?")
    interest_type = input(str("Please enter interest type:\nsimple\ncompound\n"))

    #choose type of interest
    if interest_type == "simple":
        print("You have chosen Simple interest")
        total = principle * (1 + rate * time)
       
    #compound interest
    elif interest_type == "compound":
        print("You have chosen compound interest")
        total = principle * pow((1 + rate), time)
    else:
        print("invalid request!")

    print(f"Balance after {time} years: £{total:.2f}")

    #calculating bond
else:
    if calculator_choice == 'bond' or calculator_choice =="BOND" or  calculator_choice =='Bond':
        
        #variables
        house_value = 0
        bond_rate = 0
        time = 0
        interest = ((bond_rate / 100 )/12)
    
        house_value = float(input("Enter house value: "))
        bond_rate = float(input("Enter interest rate: "))  
        time = int(input("Enter time in months: "))
        bond_interest = ((bond_rate / 100 )/12)
       
    #printing out the outputs
        print("£",house_value)
        print(bond_rate,"%")
        print(time, "months")
        print(bond_interest)

    # Bond repayment calculation 
        repayment = ((bond_interest * house_value)/(1-(1 + bond_interest) ** (-time)))
        print(f"Total monthly repayment: £{repayment}")

    else:
        #Error message
        print("Invalid Entry ")







  





















