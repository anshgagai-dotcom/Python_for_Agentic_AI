"""Task 15 — Duplicate Remover (order preserve)
Ek list nums = [3, 1, 2, 3, 4, 1, 5, 2] lo. Duplicates hatao par original order bana rahe. (Sirf set(nums) order tod dega — isliye set ko sirf "dekha kya" check ke liye use karo.)

Concepts: set for membership, list, for loop, .append()
Hint: ek seen = set() rakho. Har num par: agar num not in seen, toh result mein append karo aur seen.add(num)."""




nums = [3, 1, 2, 3, 4, 1, 5, 2]
seen = set()
result = []

for num in nums:

    if num not in seen:
        result.append(num)
        seen.add(num)

print("Original List :", nums)
print("Without Duplicates :", result)
