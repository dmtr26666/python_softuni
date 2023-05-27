budget = float(input())
season = str(input())

destination = ''
type_of_holiday = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.3
        type_of_holiday = 'Camp'
    else:
        type_of_holiday = 'Hotel'
        price = budget * 0.7
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.4
        type_of_holiday = 'Camp'
    else:
        type_of_holiday = 'Hotel'
        price = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    type_of_holiday = 'Hotel'
    price = budget * 0.9

print(f"Somewhere in {destination}" )
print(f"{type_of_holiday} - {price:.2f}")
