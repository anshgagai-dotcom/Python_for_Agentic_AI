# Backoff calculate karke print karo: 4 attempts ke liye wait times (delay=1).
# Calculate and print the backoff times for 4 attempts using delay=1.


delay = 1

for attempt in range(1, 5):
    wait_time = delay * (2 ** (attempt - 1))
    print(f"Attempt {attempt}: wait {wait_time} seconds")