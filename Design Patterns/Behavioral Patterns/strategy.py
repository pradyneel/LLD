from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv, expiry_date):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date
    
    def pay(self, amount: float):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount: float):
        print(f"Paid {amount} using Paypal.")

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def pay(self, amount: float):
        print(f"Paid {amount} using Bitcoin.")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def execute_payment(self, amount: float):
        self._strategy.pay(amount)

if __name__ == '__main__':
    payment = PaymentContext(CreditCardPayment("1234-5678-9012-3456", "123", "12/24"))
    payment.execute_payment(250.0)

    payment.set_strategy(PayPalPayment("user@example.com"))
    payment.execute_payment(100.0)