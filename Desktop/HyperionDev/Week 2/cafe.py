
menu = ['tea', 'sugar', 'coffee', 'croisants', 'butter', 'hashbrowns'] #menu list that is available to order in the cafe

stock_dictionary = {'tea': 8, 'sugar': 15, 'coffee': 19, 'croisants': 3, 'butter': 4, 'hashbrowns': 4} #dictionary storing the stock that is available to be used to create menu items

price_dictionary = {'tea': 3.60, 'sugar': 1.80, 'coffee': 6.35, 'croisants': 4.10, 'butter': 3.75, 'hashbrowns': 1.80} #price dictionary

#to calculate stock levels, the program needs to loop over the menu list 
total_value_of_stock = 0 #here, we are creatign the variable to store stoke value

#the For Loop is used to iterate over the menu
for item in menu:
    value_of_item = (stock_dictionary[item] * price_dictionary[item]) #value of item is the variable that will store the full value of the current item
    total_value_of_stock += value_of_item #this calculates the total amount

print(f"The total value of stock counted is: \n £{total_value_of_stock:.2f} ") # an f-string is used and this line of code will print the total value of the stock in pounds. The string has been formated to two significant figure
