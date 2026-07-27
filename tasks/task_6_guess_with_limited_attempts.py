"""Ek secret number fix karo (secret = 42). User ko sirf 3 chances do guess karne ke. Har galat guess par "Too high" / "Too low" batao. 3 ke andar sahi → "You won", warna → "Game over, number was 42".

Concepts: while, break, counter, if/elif/else
Hint: attempts counter rakho, while attempts < 3. Sahi guess par break"""



"""secret = 42
attempts = 0

while attempts < 3:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == secret:
        print("You Won!")
        break
    elif guess < secret:
        print("Too Low!")
    else:
        print("Too High!")

if guess != secret:
    print(f"Game Ower! The number was {secret}.")"""





"""secret = 50
attempts = 0

while attempts < 3:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1


    if guess == secret:
        print("You Won!")
        break

    elif guess < secret:
        print("Too Low!")   

    else:
        print("Too High")


if guess != secret:
    print(f"Game Ower! The secret number was {secret}")"""






"""secret = 61
attempts = 0

while attempts < 3:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == secret:
        print("You Won!")
        break
    elif guess < secret:
        print("Too Low!")
    else:
        print("Too High!")

if guess != secret:
    print(f"Game Ower! The secret number was {secret}")"""







secret = 35
attempts = 0

while attempts < 3:
    print("\n=================")
    guess = int(input("Enter the guess: "))
    attempts = attempts + 1

    if guess == secret:
        print("You Won!")
        break
        
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")
        print("=" * 35)

if guess != secret:
    print(f"Game Ower! the secret number was {secret}")
    print("=" * 35)
    




