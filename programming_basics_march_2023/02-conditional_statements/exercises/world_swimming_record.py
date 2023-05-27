import math
from math import floor
current_record = float(input())
distance_in_meters = float(input())
sec_per_meter = float(input())

resistance = (math.floor(distance_in_meters / 15) * 12.5)
time_to_swim = distance_in_meters * sec_per_meter + resistance

if time_to_swim < current_record:
    print(f'Yes, he succeeded! The new world record is {time_to_swim:.2f} seconds.')
else:
    seconds_needed = abs(current_record - time_to_swim)
    print(f'No, he failed! He was {seconds_needed:.2f} seconds slower.')
