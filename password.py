import time

password = 12345678
login = 87654321
i = 0

while True:
    password_input = int(input("Enter password: "))
    login_input = int(input("Enter login: "))
    if password_input == password and login_input == login:
        print("You have successfully entered!!!")
        break
    else:
        i += 1
        if i > 3:
            print("Wrong password or login!(5 sec ban)")
            time.sleep(5)
        else:
            print("Wrong password or login!")
