type_of_flower = str(input())
quantity = int(input())
budget = int(input())
price = 0
discount = 0

if type_of_flower == 'Roses':
    price = 5
    if quantity > 80:
        discount += 0.1
elif type_of_flower == 'Dahlias':
    price = 3.80
    if quantity > 90:
        discount += 0.15
elif type_of_flower == 'Tulips':
    price = 2.80
    if quantity > 80:
        discount += 0.15
elif type_of_flower == 'Narcissus':
    price = 3
    if quantity < 120:
        discount -= 0.15
elif type_of_flower == 'Gladiolus':
    price = 2.50
    if quantity < 80:
        discount -= 0.2

total_sum = quantity * price * (1 - discount)
diff = abs(budget - total_sum)

if total_sum <= budget:
    print(f"Hey, you have a great garden with {quantity} {type_of_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")