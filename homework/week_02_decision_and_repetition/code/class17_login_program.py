#1
"""username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")"""


#2
"""username = input("Username: ")
password = input("Password: ")

if username != "admin":
    print("Incorrect Username")
elif password != "1234":
    print("Incorrect Password")
else:
    print("Login Successful")"""    


#3
"""correct_password = "python123"
attempt = 0

while attempt < 3:
    password = input("Enter Password: ")

    if password == correct_password:
        print("Login Successful")
        break
    else:
        attempt += 1
        print("Wrong Password")

if attempt == 3:
    print("Account Locked")"""   


#4
"""username = input("Username: ")
password = input("Password: ")
otp = input("Enter OTP: ")

if username == "admin" and password == "1234" and otp == "5678":
    print("Login Successful")
else:
    print("Access Denied")"""


#5
"""username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Welcome Admin")
elif username == "user" and password == "5678":
    print("Welcome User")
else:
    print("Invalid Login")"""



