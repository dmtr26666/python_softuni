tabs_count = int(input())
salary = int(input())

fine_amount = 0

for i in range(tabs_count):
    tab_name = str(input())
    if tab_name == "Facebook":
        fine_amount += 150
    elif tab_name == "Instagram":
        fine_amount += 100
    elif tab_name == "Reddit":
        fine_amount += 50

diff = abs(salary - fine_amount)

if salary <= fine_amount:
    print("You have lost your salary.")
else:
    print(diff)
