projection = str(input())
rows = int(input())
cols = int(input())
income = 0

cinema_capacity = rows * cols

if projection == 'Premiere':
    income = cinema_capacity * 12.00
elif projection == 'Normal':
    income = cinema_capacity * 7.50
elif projection == 'Discount':
    income = cinema_capacity * 5.00

print(f'{income:.2f} leva')