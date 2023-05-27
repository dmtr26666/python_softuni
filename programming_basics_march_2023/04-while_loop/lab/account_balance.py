balance = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        print(f"Total: {balance:.2f}")
        break
    elif float(command) < 0:
        print('Invalid operation!')
        print(f"Total: {balance:.2f}")
        break

    print(f"Increase: {float(command):.2f}")
    balance += float(command)


