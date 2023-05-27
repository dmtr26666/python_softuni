book = input()

books_checked = 0

while True:
    current_book = input()

    if current_book == book:
        print(f'You checked {books_checked} books and found it.')
        break
    elif current_book == "No More Books":
        print('The book you search is not here!')
        print(f'You checked {books_checked} books.')
        break
    else:
        books_checked += 1
