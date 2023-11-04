#Create file called full_name.py

#variables to store the user name and user surname
name = input("Enter your name: \n ")
surname = input("Enter your Surname: \n ")

#Adds together the name and surname and formats it
full_name = f"{name} {surname}"

#Checks if the user has enter in their name 
if len(full_name) == 0:
    print("You have not entered anything!")

#Alerts user that their name is too short 
elif len(full_name)< 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

#Alerts user that their name is too short 
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

else:
    print(full_name)

    print("Thank you for entering your name")





