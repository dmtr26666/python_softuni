days_staying = int(input()) - 1
type_of_room = str(input())
grade = str(input())

price = 0
discount = 0

if type_of_room == "room for one person":
    price = 18
elif type_of_room == "apartment":
    price = 25
    if days_staying < 10:
        discount += 0.3
    elif 10 <= days_staying <= 15:
        discount += 0.35
    elif days_staying > 15:
        discount += 0.5
elif type_of_room == "president apartment":
    price = 35
    if days_staying < 10:
        discount += 0.1
    elif 10 <= days_staying <= 15:
        discount += 0.15
    elif days_staying > 15:
        discount += 0.2

total = price * days_staying *(1 - discount)
if grade == 'positive':
    total = total + total * 0.25
else:
    total = total - total * 0.1

print(f'{total:.2f}')

    



