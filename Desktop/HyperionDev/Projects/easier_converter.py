
import requests

response = requests.get("https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD,GBP")
exchange_rates = response.json()["rates"]

#ask the user the amount they want to exchange and the currency

amount = float(input("Enter the amount that you want to exchange: \n "))
from_currency = input("Enter the currency you want change from:  \n ")
to_currency = input("Enter the currency you want change to: \n ")

if from_currency == "EUR":
    from_rate = 1

else:
    from_rate = exchange_rates[from_currency]

if to_currency == "EUR":
    to_rate = 1

else:
    to_rate = exchange_rates[to_currency]

result = amount * (to_rate/ from_rate)

print(f"{amount:.2f} {from_currency} is equal to {result:.2f} {to_currency}")