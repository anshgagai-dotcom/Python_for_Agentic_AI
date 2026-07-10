#1
"""import random

secret_number = random.randint(0, 9)

for i in range(5):

    guess = int(input("Enter number: "))

    if guess == secret_number:
        print("Congratulations!")
        break

    elif guess > secret_number:
        print("Too High")

    else:
        print("Too Low")

else:
    print("Game Over")
    print(secret_number)"""






#2
"""secret_number = 7

for i in range(3):

    guess = int(input("Guess: "))

    if guess == secret_number:
        print("Correct")
        break
else:
    print("Game Over")"""




#3
"""import random

secret = random.randint(1, 5)

for i in range(3):
    guess = int(input("Enter Guess: "))

    if guess == secret:
        print("You Win")
        break
else:
    print("You Lose")"""    




#4
"""secret = 6

guess = int(input("Guess: "))

if guess > secret:
    print("Too High")
elif guess < secret:
    print("Too Low")
else:
    print("Correct")"""





#5
"""while True:

    secret = 5

    guess = int(input("Guess: "))

    if guess == secret:
        print("Correct")

    choice = input("Play Again (yes/no): ").lower()

    if choice == "no":
        break"""

        