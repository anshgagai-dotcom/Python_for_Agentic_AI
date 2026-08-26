# Run the retry function on a task that fails the first 2 times and then succeeds.
# retry function ko ek aise task par chalao jo pehle 2 baar fail kare phir success de.


attempts = 0

def sometimes_fails():
    global attempts
    attempts += 1

    if attempts < 3:
        raise ValueError("Temporary problem")

    return "Task completed successfully!"


def retry(func, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except ValueError as e:
            print(f"Attempt {attempt} failed: {e}")

    raise ValueError("All attempts failed")


print(retry(sometimes_fails))