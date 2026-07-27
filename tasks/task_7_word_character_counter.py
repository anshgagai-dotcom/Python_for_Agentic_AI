"""Task 7 — Word & Character Counter
User se ek sentence lo. Print karo: kitne words hain, kitne characters (spaces chhod kar), aur sentence UPPERCASE mein.

Concepts: .split(), .replace(), len(), .upper(), .strip()
Hint: spaces hatane ke liye .replace(" ", "") phir len()."""



"""sentence = input("Enter a sentence: ").strip()
words = sentence.split()
words_count = len(words)
no_spaces = sentence.replace(" ", "")
character_count = len(no_spaces)
upper_text = sentence.upper()

print("\n=========Result=========")
print(f"Words {words_count}")
print(f"Characters {character_count}")
print(f"Uppercase {upper_text}")"""








sentence = input("Enter a sentence: ").strip()
words = sentence.split()
words_counts = len(words)
no_spaces = sentence.replace(" ", "")
character = len(no_spaces)
upper_text = sentence.upper()

print("\n======Result======")
print(f"Words {words_counts}")
print(f"character {character}")
print(f"Uppercase {upper_text}")





