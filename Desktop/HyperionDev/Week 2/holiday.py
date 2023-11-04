#For this task, i will define the functions that we will be using to get the program running
#here, we are defining the cost of the nights 

def hotel_cost(num_nights): #the name of the function is hotel_cost and it stores the number of nights that the user will be wanting to book for 
    hotel_price_per_night = 300 #the price per night is fixed for all hotels across the destinations 
    total_hotel_price = (num_nights * hotel_price_per_night) #here we are we calculate the total hotel price over the number of days the user wants to stay
    return(total_hotel_price) #here, we end the loop of executing the hotel cost function

#defining the flight cost. IF statements are used to loop over the cities that the user wants to go to.
def flight_cost(city_flight):
    if city_flight == "Dubai":
        return 580 # this is the price that is returned to the user if they choose to go to Dubai
    elif city_flight == "Bali":
        return 1200
    elif city_flight == "Victoria Falls":
        return 1110
    elif city_flight == "Perth":
        return 1200
    else:
        return 0  # If a city that is not in the list is entered, nothing will be returned by the program

#defining car rental. 
def car_rental(rental_days):
    rental_price_per_day = 60 
    total_rental_cost = (rental_days * rental_price_per_day)
    return total_rental_cost

#defining the holiday costs. This will calculate the total cost of holiday including flights, hotel and car rental if any
def holiday_cost(num_nights, city_flight, rental_days): #this function includes the city flight, car rental and the number of nights that the user will be staying for
    total_hotel_price = hotel_cost(num_nights) #total hotel price
    total_flight_cost = flight_cost(city_flight) #total flight cost
    total_rental_cost = car_rental(rental_days) #total rental cost
    total_holiday_cost = total_hotel_price + total_flight_cost + total_rental_cost #the total holiday costs added together
    return total_holiday_cost

#This print statement will welcome users and shows yusers the destinations they can choose from
print("Welcome to World Travellers, we aim to satisfy all your travel desires. \nWe have the following destinations available to chose from: \nDubai \nBali \nVictoria Falls \nPerth")

city_flight = input("Please enter destination: \n ") #user input for city 
num_nights = int(input("How many nights do you want to book hotel for?: \n ")) #user hotel stay input
rental_days = int(input("How many days are you renting the car for: \n ")) #user rental car input

#this is the total holday cos variable that will be printed out 
total_holiday_cost = holiday_cost(num_nights, city_flight, rental_days)

print("The total price per person for your holiday to", city_flight, "is: £", total_holiday_cost)
