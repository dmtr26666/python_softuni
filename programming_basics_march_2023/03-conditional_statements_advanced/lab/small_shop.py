product = input()
city = input()
quantity = float(input())
bill = 0

if city == 'Sofia':
    if product == 'coffee':
        bill = quantity * 0.5
    elif product == 'water':
        bill = quantity * 0.8
    elif product == 'beer':
        bill = quantity * 1.2
    elif product == 'sweets':
        bill = quantity * 1.45
    elif product == 'peanuts':
        bill = quantity * 1.60
if city == 'Plovdiv':
    if product == 'coffee':
        bill = quantity * 0.4
    elif product == 'water':
        bill = quantity * 0.7
    elif product == 'beer':
        bill = quantity * 1.15
    elif product == 'sweets':
        bill = quantity * 1.30
    elif product == 'peanuts':
        bill = quantity * 1.50
if city == 'Varna':
    if product == 'coffee':
        bill = quantity * 0.45
    elif product == 'water':
        bill = quantity * 0.7
    elif product == 'beer':
        bill = quantity * 1.1
    elif product == 'sweets':
        bill = quantity * 1.35
    elif product == 'peanuts':
        bill = quantity * 1.55

print(bill)