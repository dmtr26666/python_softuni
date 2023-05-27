from sys import maxsize

max_number = -maxsize

while True:
    command = input()

    if command == 'Stop':
        print(max_number)
        break

    current_number = int(command)
    if current_number > max_number:
        max_number = current_number
