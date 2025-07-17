class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
        self.__transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__balance - amount
            self.__transaction_history.append(f"Deposit: {amount}")
            return f"Deposit: {amount}"
        else:
            return "Deposit must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdraw: {amount}")
            return f"Withdraw: {amount}"
        else:
            return f"Invalid withrdawal amount"

    def get_balance(self):
        return f"Balance: {self.__balance}"

    def get_transaction(self):
        return '\n'.join(self.__transaction_history)


bank_account = BankAccount(10_000)
print(bank_account.get_balance())
print(bank_account.deposit(5000))
print(bank_account.withdraw(2000))
print(f"Transactions: {bank_account.get_transaction()}")
print(bank_account.get_balance())