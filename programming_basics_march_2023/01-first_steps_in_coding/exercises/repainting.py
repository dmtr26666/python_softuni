nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_to_finish = int(input())

safety_nylon_per_cubicmeter = 1.50
paint_per_liter = 14.50
paint_thinner_per_liter = 5

nylon_total = (nylon_needed + 2) * safety_nylon_per_cubicmeter
paint_total = (paint_needed + (paint_needed * 0.10)) * paint_per_liter
thinner_total = thinner_needed * paint_thinner_per_liter
total = nylon_total + paint_total + thinner_total + 0.40

workers_fee = (total * 0.30) * hours_to_finish

print(workers_fee + total)
