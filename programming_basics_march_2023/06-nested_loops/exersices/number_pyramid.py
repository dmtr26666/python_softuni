number = int(input())

current = 1
alert = False

for rows in range(1, number + 1):
    for cols in range(1, rows + 1):
        if current > number:
            alert = True
            break
        print(current, end=" ")
        current += 1
    print()
    if alert:
        break