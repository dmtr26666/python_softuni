while True:
    money_saved = 0
    destination = input()
    if destination == "End":
        break
    money_required = float(input())
    while True:
        if money_saved >= money_required:
            print(f"Going to {destination}!")
            break
        else:
            deposit = float(input())
            money_saved += deposit