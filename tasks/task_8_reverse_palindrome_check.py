"""Task 8 — Reverse & Palindrome Check
User se ek word lo. Use ulta print karo, aur batao woh palindrome hai ya nahi (case ignore karo — "Madam" bhi palindrome hai).

Concepts: slicing [::-1], .lower(), if/else
Hint: compare karne se pehle dono ko .lower() kar do."""



word = input("Enter a word: ")
word = word.lower()
reverse_word = word[::-1]

print(f"Reversed Word : {reverse_word}")

if word == reverse_word:
    print("It is a Palindrome.")
else:
    print("It is NOT a Palindrome.")

