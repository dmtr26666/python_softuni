budget = int(input())
season = str(input())
number_of_fisherman = int(input())

price = 0
discount = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if number_of_fisherman <= 6:
    discount += 0.1
elif 7 < number_of_fisherman <= 11:
    discount += 0.15
elif number_of_fisherman > 12:
    discount += 0.25

total_price = price * (1 - discount)
if number_of_fisherman % 2 == 0 and season != 'Autumn':
    total_price *= 0.95

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
