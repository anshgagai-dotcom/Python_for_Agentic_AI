"""Task 13 — Vowel & Consonant Counter
User se ek sentence lo. Ek dictionary banao jo har vowel (a,e,i,o,u) kitni baar aaya woh count kare. Phir total consonants (letters jo vowel nahi) alag se print karo.

Concepts: loop over string, dict, .get() ya in check, .lower()
Hint: counts[ch] = counts.get(ch, 0) + 1 — yeh missing key ko safely handle karta hai."""





sentence = input("Enter a sentence: ")
sentence = sentence.lower()
counts = {}
consonants = 0
for ch in sentence:
    if ch in "aeiou":
        counts[ch] = counts.get(ch, 0) + 1

    elif ch.isalpha():
        consonants += 1

print("\n===== Vowel Counts =====")

for vowel in "aeiou":
    print(f"{vowel} : {counts.get(vowel, 0)}")

print(f"\nTotal Consonants : {consonants}")
