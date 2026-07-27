"""Task 14 — Word Frequency Counter
Ek paragraph string lo (multi-word). Har word kitni baar aaya, ek dictionary mein count karo (case-insensitive). Phir sabse zyada aane wala word batao.

Concepts: .lower(), .split(), dict counting, max(..., key=...)
Hint: max(counts, key=counts.get) sabse badi value waali key deta hai."""





paragraph = input("Enter a paragraph: ")
paragraph = paragraph.lower()
words = paragraph.split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print("\n===== Word Frequency =====")
for word, count in counts.items():
    print(f"{word} : {count}")

most_word = max(counts, key=counts.get)

print(f"\nMost Frequent Word : {most_word} ({counts[most_word]} times)")
