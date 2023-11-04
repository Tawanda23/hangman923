def hotel_cost(num_nights):
    price_per_night = 100 # example price per night
    total_cost = price_per_night * num_nights
    return total_cost

def plane_cost(city_flight):
    if city_flight == "New York":
        return 500 # example flight cost
    elif city_flight == "London":
        return 800 # example flight cost
    elif city_flight == "Tokyo":
        return 1000 # example flight cost
    else:
        return 0 # invalid city input

def car_rental(rental_days):
    daily_rental_cost = 50 # example daily rental cost
    total_cost = daily_rental_cost * rental_days
    return total_cost

def holiday_cost(city_flight, num_nights, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_flight_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    total_cost = total_hotel_cost + total_flight_cost + total_car_rental_cost
    return total_cost

# Get user inputs
city_flight = input("Which city will you be flying to? (New York/London/Tokyo): ")
num_nights = int(input("How many nights will you be staying at a hotel? "))
rental_days = int(input("How many days will you be renting a car for? "))

# Calculate total cost of the holiday
total_cost = holiday_cost(city_flight, num_nights, rental_days)

# Print the total cost
print("The total cost of your holiday is: $", total_cost)
