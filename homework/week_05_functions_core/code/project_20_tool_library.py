"""
Project 20 — Build Your First Tools Library (capstone)
EN: Create a file my_tools.py with 4 reusable functions, each returning a value: celsius_to_f(c), bmi(weight, height), is_prime(n), and word_count(text). Test all four and print the results. This is the seed of your own "AI tools" library!
हिंदी: एक file my_tools.py बनाओ जिसमें 4 reusable functions हों, हर एक value return करे: celsius_to_f(c), bmi(weight, height), is_prime(n), और word_count(text)। चारों को test करके results print करो। यह आपकी अपनी "AI tools" library की शुरुआत है!
Concepts: multiple functions, return, loops/flags inside functions, .split()
Hint: For is_prime, use a flag: assume prime, loop 2..n-1, if any divides evenly set flag False. For word_count, return len(text.split()).

"""
# Step 1 >> Restate >>
# Create four reusable functions:
# 1. Convert Celsius to Fahrenheit
# 2. Calculate BMI
# 3. Check whether a number is prime
# 4. Count the number of words in a sentence


# Step 2 >> Example >>
# Celsius = 36.9 → 98.42°F
# Weight = 70 kg, Height = 1.75 m → BMI = 22.86
# Number = 17 → Prime = True
# Text = "Hello, how are you?" → Word Count = 4



# Step 3 >> Pseudocode >>
# Create function celsius_to_f(c)
#     return Fahrenheit

# Create function bmi(weight, height)
#     return BMI

# Create function is_prime(n)
#     if n < 2 return False
#     assume number is prime
#     check divisibility from 2 to n-1
#     if divisible
#         mark as not prime
#     return result
# Create function word_count(text)
#     split the text into words
#     return total number of words
# Call all four functions
# Print each returned result


# Step 4 >> Translate
def celsius_to_f(c):
    return (c * 1.8) + 32


def bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def is_prime(n):
    if n < 2:
        return False

    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    return prime


def word_count(text):
    return len(text.split())


print("The temp in fahrenheit is:", celsius_to_f(36.9))

print("The BMI is:", bmi(70, 1.75))

print("Is 17 a prime number?", is_prime(17))

print("The word count is:", word_count("Hello, how are you?"))


# Step 5 >> Trace (Dry Run)
# Function: celsius_to_f(36.9)
# c = 36.9
# return (36.9 × 1.8) + 32
# return 98.42

# Function: bmi(70, 1.75)
# weight = 70
# height = 1.75
# return 70 / (1.75²)
# return 22.857...

# Function: is_prime(17)
# n = 17
# prime = True
# i = 2 → 17 % 2 != 0
# i = 3 → 17 % 3 != 0
# ...
# i = 16 → 17 % 16 != 0
# Loop ends
# return True

# Function: word_count("Hello, how are you?")
# text.split()
# ["Hello,", "how", "are", "you?"]
# len(...) = 4
# return 4

