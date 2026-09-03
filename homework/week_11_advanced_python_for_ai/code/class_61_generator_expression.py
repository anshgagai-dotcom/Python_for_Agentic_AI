# Generator expression se 1-100 ke squares ka sum nikaalo.
# 3. Create a generator expression that calculates the sum of squares from 1 to 100.


result = sum(num * num for num in range(1, 101))

print(result)
