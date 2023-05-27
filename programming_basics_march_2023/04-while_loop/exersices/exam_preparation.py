limit = int(input())
bad_grades = 0
exersices_count = 0
grades = 0
last_exersice_name = ''
while True:
    exercise_name = input()
    if exercise_name != "Enough":
        grade = int(input())

    if exercise_name == "Enough":
        average_grade = grades / exersices_count
        print(f'Average score: {average_grade:.2f}')
        print(f'Number of problems: {exersices_count}')
        print(f'Last problem: {last_exersice_name}')
        break
    elif grade <= 4.00:
        bad_grades += 1
        last_exersice_name = exercise_name
        grades += grade
        exersices_count += 1

        if bad_grades == limit:
            print(f'You need a break, {bad_grades} poor grades.')
            break
    else:
        last_exersice_name = exercise_name
        grades += grade
        exersices_count += 1

