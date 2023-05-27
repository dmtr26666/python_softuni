years = int(input())
washing_machine_price = float(input())
price_for_toy = int(input())

toys_count = 0
money_given = 0
money_raised = 0

for i in range(1, years + 1):
    if i % 2 == 0:
        money_given += 10
        money_raised += money_given - 1
    else:
        toys_count += 1

money_from_toys = toys_count * price_for_toy

total_money = money_raised + money_from_toys

diff = abs(washing_machine_price - total_money)

if washing_machine_price <= total_money:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")