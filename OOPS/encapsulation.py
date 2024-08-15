class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds.")
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1234, 1000)
account.deposit(1000)
account.withdraw(5000)
account.withdraw(500)

print(account.get_balance())