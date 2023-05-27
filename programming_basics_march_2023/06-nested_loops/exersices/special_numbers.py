n = int(input())


for i in range (1111, 10000):
    number = str(i)
    flag = False
    for y in range(len(number)):
        index = int(number[y])

        if index == 0 or n % index != 0:
            flag = True
            break

    if not flag:
        print(i, end=' ')