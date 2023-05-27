length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

tank_volume_in_cubic_decemeters = (length * width * height) / 1000
tank_volume_with_sand = tank_volume_in_cubic_decemeters - (tank_volume_in_cubic_decemeters * percent)

print(tank_volume_with_sand)