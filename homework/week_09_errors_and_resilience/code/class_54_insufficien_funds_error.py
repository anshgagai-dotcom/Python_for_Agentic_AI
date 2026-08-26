# Ek BankAccount class (Week 7) mein withdraw ko custom InsufficientFundsError raise karwao.
# In the BankAccount class (Week 7), make the withdraw method raise a custom InsufficientFundsError when there is not enough balance.



class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError("You don't have enough money")

        self._balance -= amount
        return self._balance


account = BankAccount(100)

try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e) 