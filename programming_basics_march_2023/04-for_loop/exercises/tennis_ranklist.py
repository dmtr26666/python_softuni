from math import floor
tournaments_count = int(input())
starting_points = int(input())

points_winned = 0
tournaments_winned = 0

for _ in range(tournaments_count):
    stage_reached = str(input())
    if stage_reached == "W":
        points_winned += 2000
        tournaments_winned += 1
    elif stage_reached == "F":
        points_winned += 1200
    elif stage_reached == "SF":
        points_winned += 720

average_points_per_tournament = points_winned / tournaments_count
winning_percentage = (tournaments_winned / tournaments_count) * 100

print(f"Final points: {points_winned + starting_points}")
print(f"Average points: {floor(average_points_per_tournament)}")
print(f"{winning_percentage:.2f}%")