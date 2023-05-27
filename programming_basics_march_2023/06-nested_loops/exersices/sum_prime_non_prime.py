
prime_sum = 0
non_prime_sum = 0


while True:
    command = input()
    if command == 'stop':
        print(f"Sum of all prime numbers is: {prime_sum}")
        print(f"Sum of all non prime numbers is: {non_prime_sum}")
        break
    elif int(command) < 0:
        print("Number is negative.")
        continue

    number = int(command)
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1

    if counter > 2:
        non_prime_sum += number
    else:
        prime_sum += number




