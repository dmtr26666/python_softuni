number_of_rooms = int(input())

total_free_chairs = 0

for room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()

    chairs = chairs_and_visitors[0].count('X')
    visitors = int(chairs_and_visitors[1])

    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room}")
        total_free_chairs -= visitors - chairs
    else:
        total_free_chairs += chairs - visitors

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")