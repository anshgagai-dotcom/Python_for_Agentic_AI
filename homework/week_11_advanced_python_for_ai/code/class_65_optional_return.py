# Ek function jo int | None return kare (mile toh number, nahi toh None).
# Write a function that returns int | None (return a number if found; otherwise, return None).



def find_number(numbers: list[int], target: int) -> int | None:
    if target in numbers:
        return target
    return None


print(find_number([10, 20, 30, 40], 30))   
print(find_number([10, 20, 30, 40], 50))   

