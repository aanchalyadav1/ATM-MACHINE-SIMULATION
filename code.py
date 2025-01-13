class ATM:
    def __init__(self):
        self.balance = 1000  # Example starting balance
        self.pin = '1234'
        self.transactions = []

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")
        self.transactions.append(f"Balance inquiry: {self.balance}")

    def deposit_cash(self, amount):
        self.balance += amount
        print(f"You have deposited: {amount}")
        print(f"New balance: {self.balance}")
        self.transactions.append(f"Deposited: {amount}")

    def withdraw_cash(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"You have withdrawn: {amount}")
            print(f"Remaining balance: {self.balance}")
            self.transactions.append(f"Withdrew: {amount}")

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            print("PIN changed successfully")
            self.transactions.append("PIN changed")
        else:
            print("Incorrect old PIN")

    def show_transactions(self):
        print("Transaction history:")
        for transaction in self.transactions:
            print(transaction)


if __name__ == "__main__":
    atm = ATM()
    atm.check_balance()
    atm.deposit_cash(500)
    atm.withdraw_cash(200)
    atm.change_pin('1234', '4321')
    atm.show_transactions()
