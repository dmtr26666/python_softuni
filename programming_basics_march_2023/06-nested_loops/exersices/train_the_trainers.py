presenation_count = 0
total_sum_of_grades = 0

jourie_count = int(input())

while True:
    command = input()
    if command == "Finish":
        print(f"Student's final assessment is {total_sum_of_grades / presenation_count:.2f}.")
        break

    sum_of_grades = 0

    for i in range(jourie_count):
        grade = float(input())
        sum_of_grades += grade

    presentation_average = sum_of_grades / jourie_count
    print(f"{command} - {presentation_average:.2f}.")
    presenation_count += 1
    total_sum_of_grades += presentation_average

