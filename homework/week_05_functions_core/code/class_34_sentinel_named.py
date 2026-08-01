# Create a sentinel named _MISSING and write a function that tells whether a value was given or not given.
# Ek sentinel _MISSING banake ek function likho jo "given vs not given" bataye.

#1
"""_MISSING = object()

def check(value=_MISSING):
    if value is _MISSING:
        return "No value was given."
    return f"Value given: {value}"

print(check())"""




#2
"""_MISSING = object()

def check(value=_MISSING):
    if value is _MISSING:
        return "No value was given."
    return f"Value given: {value}"

print(check(10))"""


#3
_MISSING = object()

def check(value=_MISSING):
    if value is _MISSING:
        return "No value was given."
    return f"Value given: {value}"

print(check("Ansh, Python for Agentic AI"))


