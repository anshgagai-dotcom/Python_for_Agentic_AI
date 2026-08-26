# Write a program that accesses an index from a list and handles ValueError and IndexError separately.
# Ek program jo list se index access kare, ValueError aur IndexError dono alag handle kare



numbers = [10, 20, 30]

try:
    index = int(input("Enter an index: "))
    print(f"Value: {numbers[index]}")

except ValueError:
    print("Please enter a number.")

except IndexError:
    print("That index does not exist in the list.")
