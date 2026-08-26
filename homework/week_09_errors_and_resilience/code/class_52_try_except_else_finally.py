# Ek try/except/else/finally ka poora example likho jo chaaron blocks dikhaye.
# Write a complete try/except/else/finally example that demonstrates all four blocks.


try:
    number = int("25")
except ValueError:
    print("Something went wrong")
else:
    print(f"Conversion successful: {number}")
finally:
    print("Program finished")