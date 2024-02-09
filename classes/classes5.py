class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit {amount} accepted.Balance: {self.balance}")
        else:
            print("Invalid deposit number.Please deposit a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal {amount} accepted.Balance: {self.balance}")
            else:
                print("Withdrawal denied.")
        else:
            print("Invalid withdrawal number.Please withdraw a positive number.")


