from classes.account import Account

class SavingsAccount(Account):
    MIN_BALANCE = 1000
    WITHDRAWL_FEE = 200

    def add_interest(self, rate):
        interest_amount = self.balance * rate / 100
        self.balance += interest_amount
        return interest_amount