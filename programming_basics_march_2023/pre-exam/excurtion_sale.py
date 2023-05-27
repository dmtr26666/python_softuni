sea_trips = int(input())
mountain_trips = int(input())

total_profit = 0

while True:
    type = input()
    if type == 'Stop':
        break
    elif type == 'sea':
        if sea_trips == 0:
            continue
        else:
            total_profit += 680
            sea_trips -= 1
    elif type == 'mountain':
        if mountain_trips == 0:
            continue
        else:
            total_profit += 499
            mountain_trips -= 1

    if sea_trips == 0 and mountain_trips == 0:
        break

if sea_trips == 0 and mountain_trips == 0:
    print("Good job! Everything is sold.")
    print(f"Profit: {total_profit} leva.")
else:
    print(f"Profit: {total_profit} leva.")
