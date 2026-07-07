print("========== Password Limit Attempts Program ==========")

user_name = "golu123"
password = "agentic_ai"

attempts = 0

while attempts < 3:
    entered_user = input("Enter username: ")
    entered_password = input("Enter password: ")

    if entered_user != user_name:
        print("Incorrect username!")
        attempts += 1

    elif entered_password != password:
        print("Incorrect password!")
        attempts += 1

    else:
        print("Login Successful!")
        break

    print(f"Attempts left: {3 - attempts}")

if attempts == 3:
    print("Account Locked!")