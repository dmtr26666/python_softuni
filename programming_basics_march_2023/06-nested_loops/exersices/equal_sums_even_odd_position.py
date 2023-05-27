starting_number = int(input())
ending_number = int(input())

for i in range(starting_number, ending_number + 1):
    odd_sum = 0
    even_sum = 0
    number = str(i)
    for y in range(len(number)):
        index = int(number[y])
        if y % 2 == 0:
            even_sum += index
        else:
            odd_sum += index

    if odd_sum == even_sum:
        print(i, end=' ')