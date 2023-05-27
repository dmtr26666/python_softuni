dancers_count = int(input())
points = float(input())
season = input()
place = input()


if place == "Bulgaria":
    money_winned = points * dancers_count
    if season == 'winter':
        money_winned *= 0.92
    elif season == 'summer':
        money_winned *= 0.95
else:
    money_winned = (points * dancers_count) * 1.50
    if season == 'winter':
        money_winned *= 0.85
    elif season == 'summer':
        money_winned *= 0.90

money_for_charity = money_winned * 0.75
money_left = money_winned - money_for_charity

print(f"Charity - {money_for_charity:.2f}")
print(f"Money per dancer - {money_left / dancers_count:.2f}")



