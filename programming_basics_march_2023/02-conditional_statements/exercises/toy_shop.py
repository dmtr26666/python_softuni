excursion_price = float(input())
puzzel_count = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())


all_toys = puzzel_count + dolls + bears + minions + trucks
order_sum = puzzel_count * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2

if all_toys >= 50:
    order_sum *= 0.75

rent = order_sum * 0.1
profit = order_sum - rent


if profit >= excursion_price:
    profit = profit - excursion_price
    print(f"Yes! {profit:.2f} lv left.")
elif profit < excursion_price:
    profit = abs(profit - excursion_price)
    print(f'Not enough money! {profit:.2f} lv needed.')
