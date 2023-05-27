days = int(input())

total_rakia = 0
total_degree = 0

for i in range(days):
    rakia_quantity = float(input())
    degree_of_rakia = float(input())

    total_rakia += rakia_quantity
    total_degree += rakia_quantity * degree_of_rakia


average_degree = total_degree / total_rakia

print(f"Liter: {total_rakia:.2f}")
print(f"Degrees: {average_degree:.2f}")
if average_degree < 38:
    print("Not good, you should baking!")
elif 38 <= average_degree <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")