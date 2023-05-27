month = str(input())
night_count = int(input())

price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    price_apartment = night_count * 65
    price_studio = night_count * 50
    if 7 < night_count <= 14:
        price_studio *= 0.95
    elif night_count > 14:
        price_studio *= 0.7
        price_apartment *= 0.9
elif month == 'June' or month == 'September':
    price_apartment = night_count * 68.70
    price_studio = night_count * 75.20
    if night_count > 14:
        price_studio *= 0.8
        price_apartment *= 0.9
elif month == 'July' or month == 'August':
    price_studio = night_count * 76
    price_apartment = night_count * 77
    if night_count > 14:
        price_apartment *= 0.9



print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')
