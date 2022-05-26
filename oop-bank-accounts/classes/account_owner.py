from classes.read_csv import CsvHelper

class AccountOwner:
    FILE_NAME = "../support/account_owners.csv"

    def __init__(self, account_id, owner_id):
        self.account_id = account_id
        self.owner_id = owner_id

    def __repr__(self):
        return f"ACCT: {self.account_id} / OWNER: {self.owner_id}"

    @classmethod
    def load_all_account_owners(cls):
        return CsvHelper.read_all(cls.FILE_NAME, cls)

    @classmethod
    def save_account_owner(cls, new_account_owner):
        return CsvHelper.write_one(cls.FILE_NAME, new_account_owner)

    @classmethod
    def save_all_account_owners(cls, account_owners):
        return CsvHelper.write_all(cls.FILE_NAME, account_owners)