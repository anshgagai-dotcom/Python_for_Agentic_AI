# Safe int conversion: user input ko int banao, ValueError handle karke "Invalid" bolo.
# Safe int conversion: Convert user input into an integer, handle ValueError, and print "Invalid".



text = input("Enter a whole number: ")

try:
    number = int(text)
    print(f"Your number is: {number}")
except ValueError:
    print("Invalid")
