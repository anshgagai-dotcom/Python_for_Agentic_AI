# step 1 >> restate : create simple calculator for +, -, *, /.
# step 2 >> example : 7 + 9 >> 16
# step 3 >> Pseudocode :
       # Take two input number from user
       # Take any one operator as input (+, -, *, /)
       # call respective function according to user input operator
# step 4 >> Translate to Python code
# step 5 >> Trace (Dry Run)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2 


def div(num1, num2):
    return num1/ num2   
     
print("========== Welcome to simple calculator==========")

while True:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    operator = input("Enter the operator(+, -, *, /): ")

    if operator == "+":
        print("Addition of two numbers is: ", add(number1, number2))

    elif operator == "-":
        print("Subtraction of two numbers is: ", sub(number1, number2))

    elif operator == "*":
        print("Multiplication of two numbers is: ", multi(number1, number2))

    elif operator == "/":
        print("Division of two numbers is: ", div(number1, number2))

    else:
        print("Invalid Operator")
    print("=========================")

    want_to_continue = input("Do you want to continue? (y/n): ")
    if want_to_continue == "n":
        break
    print("=========================")

# ========== Welcome to simple calculator========
# Enter the first number: 9
# Enter the second number: 4
# Enter the operator(+, -, *, /): +
# Addition of two numbers is: 13

