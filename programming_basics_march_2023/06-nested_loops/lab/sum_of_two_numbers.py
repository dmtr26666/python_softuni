start_number = int(input())
end_number = int(input())
magic_number = int(input())

combination_count = 0
NUMBER_FOUND = False

for x in range(start_number, end_number + 1):
    for y in range(start_number, end_number + 1):
        number_sum = x + y
        combination_count += 1
        if number_sum == magic_number:
            NUMBER_FOUND = True
            print(f"Combination N:{combination_count} ({x} + {y} = {magic_number})")
            break
    if NUMBER_FOUND:
        break

if not NUMBER_FOUND:
    print(f"{combination_count} combinations - neither equals {magic_number}")