num1_limit = int(input())
num2_limit = int(input())
num3_limit = int(input())

for part1 in range(1, num1_limit + 1):
    if part1 % 2 == 0:
        for part2 in range(1, num2_limit + 1):
            if part2 == 2 or part2 == 3 or part2 == 5 or part2 == 7:
                for part3 in range(1, num3_limit + 1):
                    if part3 % 2 == 0:
                        print(f"{part1} {part2} {part3}")

