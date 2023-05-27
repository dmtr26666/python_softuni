import math
from math import ceil

series_name = str(input())
episode_length = int(input())
break_duration = int(input())

time_for_lunch = break_duration / 8
time_for_rest = break_duration / 4
time_for_serial = break_duration - (time_for_rest + time_for_lunch)

if time_for_serial >= episode_length:
    time_left = time_for_serial - episode_length
    print(f'You have enough time to watch {series_name} and left with {math.ceil(time_left)} minutes free time.')
else:
    time_needed = abs(time_for_serial - episode_length)
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(time_needed)} more minutes.")