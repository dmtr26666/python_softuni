budget = float(input())
statists = int(input())
price_per_clothing = float(input())

decor_price = budget * 0.1
clothing_price = statists * price_per_clothing

if statists > 150:
    clothing_price *= 0.9

if decor_price + clothing_price > budget:
    money_needed = abs(budget - (decor_price + clothing_price))
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
else:
    money_leftover = budget - (decor_price + clothing_price)
    print('Action!')
    print(f'Wingard starts filming with {money_leftover:.2f} leva left.')
