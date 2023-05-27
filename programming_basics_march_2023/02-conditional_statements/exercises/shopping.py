budget = float(input())
number_of_videocards = int(input())
number_of_proccecors = int(input())
number_of_rams = int(input())

videocards_price = number_of_videocards * 250

total_price = videocards_price + number_of_proccecors * (videocards_price * 0.35) + number_of_rams * (videocards_price * 0.1)

if number_of_videocards > number_of_proccecors:
    total_price *= 0.85

if total_price <= budget:
    money_left = budget - total_price
    print(f'You have {money_left:.2f} leva left!')
else:
    money_needed = abs(budget - total_price)
    print(f'Not enough money! You need {money_needed:.2f} leva more!')