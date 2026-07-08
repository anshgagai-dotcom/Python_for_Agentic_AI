import random

while True:

    secret_number = random.randint(0, 9)

    print("===== Welcome to the Game of Guessing Numbers =====")
    print("To win the game, you have only 5 attempts.\n")

    for i in range(5):

        print(f"Attempt {i + 1} of 5")

        user_guess_num = int(input("Enter the guessing number [0-9]: "))

        if user_guess_num == secret_number:
            print(f" Congrats! You guessed the number in {i + 1} attempts.")
            break

        elif user_guess_num > secret_number:
            print("Too high! Try again.")

        else:
            print("Too low! Try again.")

        print("====================")

    else:
        print("\nGame Over!")
        print(f"The secret number was: {secret_number}")

    print("=" * 50)

    user_input = input("Do you want to play again? (yes/no): ").lower()

    if user_input == "no":
        print("\nThanks for playing!")
        break

    