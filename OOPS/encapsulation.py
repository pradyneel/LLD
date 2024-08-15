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

bank_account = BankAccount(1234, 1000)
# After Account Created
print(bank_account.get_balance())

# Deposit 1000
bank_account.deposit(1000)
print(bank_account.get_balance())

# Withdraw 500
bank_account.withdraw(500)
print(bank_account.get_balance())