print("==========Password Limit Attempts Program==========")
password = "agentic_ai"
attempts = 0

while attempts < 3:
    user_password = input("Enter password: ")

    if user_password == password:
        print("Login Successful!")
        break
    else:
        print("Please enter correct password")
    attempts +=1

if attempts == 3:
    print("Account Locked!")
        






