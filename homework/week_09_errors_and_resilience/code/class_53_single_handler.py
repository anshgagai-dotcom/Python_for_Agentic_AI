# Do errors (ZeroDivisionError, ValueError) ko ek hi handler se pakdo.
# Catch two errors (ZeroDivisionError, ValueError) using a single handler.


try:
    value = int("hello")
    result = 20 / 0

except (ZeroDivisionError, ValueError) as error:
    print(f"Something went wrong: {error}")