goal = 10000

total_steps = 0

while True:
    command = input()

    if command == 'Going home':
        steps_to_home = int(input())
        total_steps += steps_to_home
        if total_steps < goal:
            diff = abs(total_steps - goal)
            print(f'{diff} more steps to reach goal.')
            break
        else:
            diff = abs(total_steps - goal)
            print(f'Goal reached! Good job!')
            print(f'{diff} steps over the goal!')
            break
    else:
        steps = int(command)
        total_steps += steps
        if total_steps >= goal:
            diff = abs(total_steps - goal)
            print("Goal reached! Good job!")
            print(f'{diff} steps over the goal!')
            break


