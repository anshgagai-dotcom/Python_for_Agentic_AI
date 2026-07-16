"""Task 3 — Even ya Odd + Positive/Negative
User se ek number lo. Batao woh positive/negative/zero hai, AUR even/odd hai (zero ke liye even/odd mat batao).

Concepts: if/elif/else, modulus %, ternary
Hint: even/odd ke liye n % 2 == 0. Ek ternary se "Even"/"Odd" choose karo."""



"""number = int(input("Enter a Number: "))

if number > 0:
    print("Number is Positive")

elif number < 0:
    print("Number is Negative")

else:
    print("Number is Zero")


if number % 2 == 0:
    print("Result: Even!")

else:
    print("Result: Odd!")"""






"""number = int(input("Enter a number: "))

if number > 0:
    print("Number is +ve")

elif number < 0:
    print("Number is -ve")

else:
    print("Number is Zero")


if number % 2 == 0:
    print("Even!")

else:
    print("Odd!") """           








number = int(input("Enter a number: "))

if number > 0:
    print("Number is Positive")

elif number < 0:
    print("Number is Negative")
else:
    print("Number is Zero")    


if number != 0:
    result = "Even!" if number % 2 == 0 else "Odd!"
    print(f"The Result is: {result}.")

