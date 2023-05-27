walk_length = int(input())
walks_per_day = int(input())
calorie_intake = int(input())

minutes_walking = walk_length * walks_per_day
burned_calories = minutes_walking * 5

if burned_calories >= calorie_intake * 0.5:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')