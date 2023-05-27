cubicmeters = float(input())
price_per_cubic = 7.61

price = cubicmeters * price_per_cubic
discount = price * 0.18
total_price = price - discount

print(f"{total_price} lv.")
print(f"{discount} lv.")