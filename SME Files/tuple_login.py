username = ("vyom", "venkat", "jeevan", "sravan", "swaroop")
passwords = ("12345", "67890", "24680", "13579", "12357")
while True:
    user_input = input("Enter username: ")
    password_input = input("Enter password: ")
    if user_input in username:
        index = username.index(user_input)
        if password_input == passwords[index]:
            print("Access granted")
            break
        else:
            print("Access denied")
    else:
        print("Access denied")
    operation = input("Enter 1 to retry the connection or 2 to exit: ")
    if operation == "1":
        continue
    elif operation == "2":
        break
    else:
        print("Invalid operation")
        break
