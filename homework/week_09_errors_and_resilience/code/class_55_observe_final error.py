# retry mein ek case add karo jahan saare attempts fail hon — aakhri error dekho.
# Add a case to retry where all attempts fail and observe the final error.


from class_55_retry_function import retry


def always_fails():
    raise ValueError("The task failed every time")


try:
    retry(always_fails, max_attempts=2)

except ValueError as e:
    print(f"Final error: {e}")