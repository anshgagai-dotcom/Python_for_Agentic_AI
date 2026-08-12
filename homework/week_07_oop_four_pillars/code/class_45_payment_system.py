"""
Create an abstract PaymentMethod class with an abstract pay(amount) method. 
Create UPIPayment and CardPayment child classes that implement pay() differently.
"""
# Ek abstract PaymentMethod with abstract pay(amount); Cash aur Card se implement karo.



from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """
    Define the rules for a payment method.
    """

    @abstractmethod
    def pay(self, amount: float) -> str:
        """
        Process a payment for the given amount.
        """
        ...


class UPIPayment(PaymentMethod):
    """
    Represent a UPI payment.
    """

    def pay(self, amount: float) -> str:
        """
        Process payment using UPI.
        """
        return f"Paid ₹{amount} using UPI"


class CardPayment(PaymentMethod):
    """
    Represent a card payment.
    """

    def pay(self, amount: float) -> str:
        """
        Process payment using a card.
        """
        return f"Paid ₹{amount} using Card"


upi = UPIPayment()
card = CardPayment()

print(upi.pay(750))
print(card.pay(1200))

