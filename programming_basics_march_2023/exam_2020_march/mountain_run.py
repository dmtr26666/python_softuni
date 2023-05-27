import math

current_record = float(input())
length_in_meters = float(input())
seconds_per_meter = float(input())

time_to_climb = length_in_meters * seconds_per_meter
slow_down = math.floor(( length_in_meters / 50 )) * 30
total_time = time_to_climb + slow_down

if total_time < current_record:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    time_needed = abs(current_record - total_time)
    print(f'No! He was {time_needed:.2f} seconds slower.')
