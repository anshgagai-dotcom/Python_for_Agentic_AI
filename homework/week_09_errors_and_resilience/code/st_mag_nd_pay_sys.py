# Student marks should be in 0 - 100 in number format

import random
import time


class InvalidMarsError(Exception):
    """Raised whn the marks are not in between 0 - 100"""
    pass

class InsufficientBalanceError(Exception):
    """Raised when the balance is less than exam fee"""
    pass


def get_valid_marks(subject_name: str) ->float:

    while True:
        try:
            raw_marks = input(f"Enter the marks for {subject_name} in between 0-100: ")
            marks = float(raw_marks)

            if marks < 0 or marks > 100:
                raise InvalidMarsError(f"Invalid marks for {subject_name}, must be in between 0-100")

            return marks

        except ValueError as e:
            print(f"Error: {e}")
        except InvalidMarsError as e:
            print(f"Error: {e}")


def simulate_bank_api(amount: float) -> str:
    """ Simulate bank API paymment processing, 50% chance of failure """

    if random.choice([True, False]):
        raise ConnectionError("Bank API is not available / Bank Gatway / Network Interrupted")
    return f"Payment of ruppes {amount:.2f} processed successful."


def process_payment_with_retry(amount: float, max_attempts: int = 3) -> str:
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"Attempt {attempt} of {max_attempts} to processing payment of ruppes {amount:.2f}")
            result = simulate_bank_api(amount)
            return result
        except ConnectionError as e:
            print(f"Attempt {attempt} failed: {e}")

            if attempt < max_attempts:
                wait = 2 ** (attempt - 1)
                time.sleep(wait)
            else:
                raise ConnectionError("Max attempts reached, payment failed")        


def main():
    print("=" * 50)
    print("Welcome to the Student Marks & Payment System")

    try:
        Student_bank_balance = 1000.00
        per_subject_exam_fee = 200

        mark_phy = get_valid_marks("Physics")
        mark_che = get_valid_marks("Chemistry")
        mark_maths = get_valid_marks("Maths")

        total_marks = mark_phy + mark_che + mark_maths
        percentage = (total_marks / 300) * 100

        if percentage < 50 or mark_phy < 50 or mark_che < 50 or mark_maths < 50:
            print("Sorry, you are failed in the exam")
            print(f"You need to pay the exam fee again")
        else:
            print(f"Congratulations, you are passed in the exam with {percentage:.2f}%")
            print("You need to pay the exam fee again")
            return  None

        total_fee = per_subject_exam_fee * 3

        if Student_bank_balance < total_fee:
            raise InsufficientBalanceError(f"Insufficient balance in the bank account, you need to pay {total_fee:.2f} ruppes")

        recepit = process_payment_with_retry(total_fee)

    except InsufficientBalanceError as e:
        print(f"Registration canceled: {e}")
    except ConnectionError as e:
        print(f"Network failure: {0}")

    else:
        print("Registration sucessful")
        print(f"Student registration recept: {recepit}")

    finally:
        print("Session closed securely. Thank you for using our system.")                    




if __name__ == "__main__":
    
    main()


                     



