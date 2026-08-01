# Intentionally create the mutable default argument bug using:
# Jaan-boojh kar def f(x=[]) waala bug banao, 3 call karke bug dikhao.

#1
"""def buggy(x=[]):

    x.append(1)
    return x

print(buggy())
print(buggy())
print(buggy())"""



#2
"""def numbers(data=[]):
    data.append(100)
    return data

print(numbers())
print(numbers())"""



#3
def colors(c=[]):
    c.append("Red")
    return c

print(colors())
print(colors())