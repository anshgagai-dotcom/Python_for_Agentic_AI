# Ek Status enum banao (PENDING, DONE, FAILED).
# Create a Status Enum with PENDING, DONE, and FAILED.


from enum import Enum

class Status(Enum):
    PENDING = "pending"
    DONE = "done"
    FAILED = "failed"


current_status = Status.PENDING

print(current_status)
print(current_status.value)

