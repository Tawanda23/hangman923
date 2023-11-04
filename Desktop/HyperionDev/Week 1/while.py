count = 0 #this is the count that will be added to each number input by the user
number = 0 # This is the number variable that the user is going to input
total = 0 # This adds together all number previous put in with the latest number

print("To exit the loop, please enter -1")

while number != -1:

    number = float(input("Please enter any number: " "\n")) #Entry will accept any number including decimals

    if number != -1:

        total = total + number

        count = count + 1 #count + 1 add one to the count number input

print("The calculated average value is: ",(total/count))


