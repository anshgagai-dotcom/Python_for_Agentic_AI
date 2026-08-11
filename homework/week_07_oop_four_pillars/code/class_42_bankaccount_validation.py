# BankAccount mein validation add karo taaki balance kabhi negative na ho.
# Add validation to the BankAccount class so that the balance can never become negative.


class BankAccount:
    """
    Represent a bank account with a protected balance.
    """

    def __init__(self, balance: int) -> None:
        """
        Initialize the account with a starting balance.
        """
        self._balance: int = balance

    def withdraw(self, amount: int) -> None:
        """
        Withdraw money only when sufficient funds are available.
        """    
        if amount > self._balance:
            print("Insufficient funds!")
            return

        self._balance -= amount

    def get_balance(self) -> int:
        """
        Return the current account balance.
        """    

account = BankAccount(1000)

account.withdraw(300)
print(account.get_balance())

account.withdraw(800)
print(account.get_balance())


