# multiply_all(*nums) jo saare numbers ka product return kare.
# Write a function multiply_all(*nums) that returns the product (multiplication) of all the numbers passed to it.


def multiply_all(*nums):

    result = 1
    for num in nums:
        result = result * num
    return result

print(multiply_all(2, 3, 4))
