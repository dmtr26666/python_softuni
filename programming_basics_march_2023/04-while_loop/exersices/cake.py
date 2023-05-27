width = int(input())
length  = int(input())

cake_pieces = width * length

while True:
    command = input()

    if command == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break
    else:
        pieces = int(command)
        cake_pieces -= pieces

        if cake_pieces <= 0:
            diff = abs(cake_pieces)
            print(f"No more cake left! You need {diff} pieces more.")
            break