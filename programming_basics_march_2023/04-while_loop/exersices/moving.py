length = int(input())
width = int(input())
height = int(input())

volume = length * height * width
volume_used = 0

while True:
    command = input()

    if command == "Done":
        diff = volume - volume_used
        print(f"{diff} Cubic meters left.")
        break
    else:
        boxes = int(command)
        volume_used += boxes

        if volume_used >= volume:
            diff = abs(volume - volume_used)
            print(f"No more free space! You need {diff} Cubic meters more.")
            break