current_hour = int(input())
current_minutes = int(input())

total_time_in_minutes = current_hour * 60 + current_minutes + 15

hours = total_time_in_minutes // 60
minutes = total_time_in_minutes % 60

if hours > 23:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')


# hour = int(input())
# minutes = int(input())
#
# new_hour = hour
# new_minutes = 0
#
#
# if minutes >= 45:
#     new_hour = hour + 1
#     new_minutes = minutes + 15
#     new_minutes = new_minutes % 60
#     if hour == 23:
#         new_hour = 0
# elif minutes < 45:
#     new_minutes = minutes + 15
#
# if new_minutes < 10:
#     print(f'{new_hour}:0{new_minutes}')
# else:
#     print(f'{new_hour}:{new_minutes}')
