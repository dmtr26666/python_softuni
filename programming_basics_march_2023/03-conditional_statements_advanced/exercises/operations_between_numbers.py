number1 = int(input())
number2 = int(input())
action = str(input())

type = ''
result = 0
ERROR = False

if action == '+':
    result = number1 + number2
    if result % 2 == 0:
        type = 'even'
    else:
        type = 'odd'
    print(f"{number1} {action} {number2} = {result} - {type}")
elif action == '-':
    result = number1 - number2
    if result % 2 == 0:
        type = 'even'
    else:
        type = 'odd'
    print(f"{number1} {action} {number2} = {result} - {type}")
elif action == '*':
    result = number1 * number2
    if result % 2 == 0:
        type = 'even'
    else:
        type = 'odd'
    print(f"{number1} {action} {number2} = {result} - {type}")
elif action == '/':
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 / number2
        print(f'{number1} / {number2} = {result:.2f}')
elif action == '%':
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 % number2
        print(f'{number1} % {number2} = {result}')



