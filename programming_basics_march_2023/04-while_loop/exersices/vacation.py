money_for_vacation = float(input())
balance = float(input())

days = 0
spend_streak = 0
while True:
    action = str(input())
    money = float(input())
    if action == 'save':
        balance += money
        spend_streak = 0
    elif action == 'spend':
        if money >= balance:
            balance = 0
        else:
            balance -= money
        spend_streak += 1
    days += 1
    if spend_streak == 5:
        print("You can't save the money.")
        print(days)
        break
    elif balance >= money_for_vacation:
        print(f"You saved the money for {days} days.")
        break