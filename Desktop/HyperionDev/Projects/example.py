import requests

# Replace YOUR_APP_ID with your actual app ID from Open Exchange Rates
app_id = 'YOUR_APP_ID'

# Define the base currency (the currency you want to convert from)
base_currency = 'USD'

# Define the currencies you want to convert to
convert_currencies = ['EUR', 'GBP']

# Build the API URL
url = f'https://openexchangerates.org/api/latest.json?app_id={app_id}&base={base_currency}'

# Fetch the exchange rates from the API
response = requests.get(url)
data = response.json()

# Extract the exchange rates for the currencies you want to convert to
exchange_rates = {}
for currency in convert_currencies:
    exchange_rates[currency] = data['rates'][currency]

# Define the amount you want to convert
amount = 100

# Define the currency you want to convert to
convert_currency = 'EUR'

#
