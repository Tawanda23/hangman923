principle = 0
rate = 0
time = 0


while True:
    principle = float(input("Enter deposit amount: "))
    if principle < 0:
        print("Deposit amount can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter time in years: "))
    if time < 0:
        print("Time can't be less than or equal to zero")
    else:
        break

print("£",principle)
print(rate,"%")
print(time, "years")

total = principle * (1 + rate * time)
print(f"Balance after {time} years: £{total:.2f}")

#compound interest
while True:
    principle = float(input("Enter deposit amount: "))
    if principle < 0:
        print("Deposit amount can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter time in years: "))
    if time < 0:
        print("Time can't be less than or equal to zero")
    else:
        break

print("£",principle)
print(rate,"%")
print(time, "years")

total = principle * pow((1 + rate), time)
print(f"Balance after {time} years: £{total:.2f}")