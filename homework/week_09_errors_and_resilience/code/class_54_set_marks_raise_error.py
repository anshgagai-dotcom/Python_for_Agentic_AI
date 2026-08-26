# Ek function set_marks(m) jo 0-100 ke bahar value par ValueError raise kare.
# Write a function set_marks(m) that raises a ValueError if the value is outside the range 0–100.



def set_marks(m):
    if m < 0 or m > 100:
        raise ValueError("Marks should be between 0 and 100")

    return m


print(set_marks(85))