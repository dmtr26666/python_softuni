student_tickets_count = 0
standard_tickets_count = 0
kids_tickets_count = 0

while True:
    film_name = input()
    if film_name == 'Finish':
        break
    hall_capacity = int(input())
    hall_capacity_left = hall_capacity
    current_tickets_count = 0
    while hall_capacity_left > 0:
        type_of_ticket = input()
        if type_of_ticket == 'End':
            break
        elif type_of_ticket == 'student':
            student_tickets_count += 1
        elif type_of_ticket == 'standard':
            standard_tickets_count += 1
        elif type_of_ticket == 'kid':
            kids_tickets_count += 1

        hall_capacity_left -= 1
        current_tickets_count += 1

    percentage_full = (current_tickets_count / hall_capacity) * 100
    print(f"{film_name} - {percentage_full:.2f}% full.")

total_tickets = standard_tickets_count + student_tickets_count + kids_tickets_count
print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets_count / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets_count / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets_count / total_tickets) * 100:.2f}% kids tickets.")
