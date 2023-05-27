name = str(input())
grade = 1
grades_sum = 0
years_failed = 0
while grade < 13:
    year_grade = float(input())

    if year_grade >= 4.00:
        grades_sum += year_grade
        grade += 1
    else:
        years_failed += 1

    if years_failed == 2:
        print(f'{name} has been excluded at {grade} grade')
        break

if grade == 13:
    average_grade = grades_sum / 12
    print(f'{name} graduated. Average grade: {average_grade:.2f}')