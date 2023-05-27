tshirt_price = float(input())
shorts_price = tshirt_price * 0.75
shocks_price = shorts_price * 0.20
shoes_price = (tshirt_price + shorts_price) * 2
discount = 0.15
price_for_discount = float(input())

total_price_with_discount = (tshirt_price + shorts_price + shocks_price + shoes_price) * (1 - discount)

if total_price_with_discount >= price_for_discount:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price_with_discount:.2f} lv.")
else:
    diff = abs(price_for_discount - total_price_with_discount)
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")

