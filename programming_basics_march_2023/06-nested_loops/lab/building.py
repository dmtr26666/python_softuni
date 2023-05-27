floors = int(input())
rooms = int(input())

for floor in reversed(range(1, floors + 1)):
    for room in range(rooms):
        if floor == floors:
            print(f"L{floor}{room}", end=' ')
        else:
            if floor % 2:
                print(f"A{floor}{room}", end=' ')
            else:
                print(f"O{floor}{room}", end=' ')

    print()
