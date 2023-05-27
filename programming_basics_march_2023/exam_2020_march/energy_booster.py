flavour = input()
size = input()
sets = int(input())


if size == 'small':
    price = 0
    if flavour == 'Watermelon':
        price = 56 * 2
    elif flavour == 'Mango':
        price = 36.66 * 2
    elif flavour == 'Pineapple':
        price = 42.10 * 2
    elif flavour == 'Raspberry':
        price = 20 * 2
else:
    if flavour == 'Watermelon':
        price = 28.7 * 5
    elif flavour == 'Mango':
        price = 19.60 * 5
    elif flavour == 'Pineapple':
        price = 24.80 * 5
    elif flavour == 'Raspberry':
        price = 15.20 * 5

total_price = price * sets

if 400 <= total_price <= 1000:
    discount = 0.15
    print(f"{total_price * (1 - discount):.2f} lv.")
elif total_price > 1000:
    discount = 0.5
    print(f"{total_price * (1 - discount):.2f} lv.")
else:
    print(f"{total_price:.2f} lv.")