from datetime import datetime
from classes.read_csv import CsvHelper

class Account:
    FILE_NAME = "../support/accounts.csv"
    MIN_BALANCE = 0
    WITHDRAWL_FEE = 0

    def __init__(self, id, balance, date = datetime.now()):
        self.id = id
        self.balance = int(balance)
        self.date = date

    def __repr__(self):
        return f"ACCT: {self.id}"

    @classmethod
    def load_all_accounts(cls):
        return CsvHelper.read_all(cls.FILE_NAME, cls)

    @classmethod
    def save_account(cls, new_account):
        return CsvHelper.write_one(cls.FILE_NAME, new_account)

    @classmethod
    def save_all_accounts(cls, accounts):
        return CsvHelper.write_all(cls.FILE_NAME, accounts)

    def withdraw(self, amount):
        new_balance = self.balance - amount - self.WITHDRAWL_FEE
        print(">>>", self.WITHDRAWL_FEE, self.MIN_BALANCE)
        if new_balance < self.MIN_BALANCE:
            print("WARNING: Can not make withdrawl due to minimum balance requirements.")
        else:
            self.balance = new_balance
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance