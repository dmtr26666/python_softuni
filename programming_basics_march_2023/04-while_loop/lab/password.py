username = input()
password = input()

while True:
    password_user = input()

    if password_user == password:
        print(f"Welcome {username}!")
        break