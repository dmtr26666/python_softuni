deposit_sum = float(input())
deposit_time = int(input())
year_interest = float(input())

interest = deposit_sum * (year_interest / 100)
print(deposit_sum + deposit_time * (interest / 12))