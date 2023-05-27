group_count = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for i in range(group_count):
    number_of_climbers = int(input())
    if number_of_climbers <= 5:
        g1 += number_of_climbers
    elif 6 <= number_of_climbers <= 12:
        g2 += number_of_climbers
    elif 13 <= number_of_climbers <= 25:
        g3 += number_of_climbers
    elif 26 <= number_of_climbers <= 40:
        g4 += number_of_climbers
    else:
        g5 += number_of_climbers

all_climbers = g1 + g2 + g3 + g4 +g5

print(f"{(g1 / all_climbers) * 100:.2f}%")
print(f"{(g2 / all_climbers) * 100:.2f}%")
print(f"{(g3 / all_climbers) * 100:.2f}%")
print(f"{(g4 / all_climbers) * 100:.2f}%")
print(f"{(g5 / all_climbers) * 100:.2f}%")