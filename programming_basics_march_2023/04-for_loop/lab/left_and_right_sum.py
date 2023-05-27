numbers = int(input())

sum1 = 0
sum2 = 0

for _ in range(numbers):
    current_number = int(input())
    sum1 += current_number

for _ in range(numbers):
    current_number = int(input())
    sum2 += current_number

diff = abs(sum1-sum2)

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
else:
    print(f'No, diff = {diff}')