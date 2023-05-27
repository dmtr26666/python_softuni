fruit = input()
day_of_week = input()
quantity = float(input())
total_sum = 0
FALSE_ALERT = False

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if fruit == 'banana':
        total_sum = quantity * 2.5
    elif fruit == 'apple':
        total_sum = quantity * 1.2
    elif fruit == 'orange':
        total_sum = quantity * 0.85
    elif fruit == 'grapefruit':
        total_sum = quantity * 1.45
    elif fruit == 'kiwi':
        total_sum = quantity * 2.7
    elif fruit == 'pineapple':
        total_sum = quantity * 5.5
    elif fruit == 'grapes':
        total_sum = quantity * 3.85
    else:
        FALSE_ALERT = True
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        total_sum = quantity * 2.7
    elif fruit == 'apple':
        total_sum = quantity * 1.25
    elif fruit == 'orange':
        total_sum = quantity * 0.9
    elif fruit == 'grapefruit':
        total_sum = quantity * 1.6
    elif fruit == 'kiwi':
        total_sum = quantity * 3
    elif fruit == 'pineapple':
        total_sum = quantity * 5.6
    elif fruit == 'grapes':
        total_sum = quantity * 4.2
    else:
        FALSE_ALERT = True
else:
     FALSE_ALERT = True

if not FALSE_ALERT:
    print(f'{total_sum:.2f}')
else:
    print('error')
