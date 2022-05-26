from classes.account import Account
from classes.owner import Owner
from classes.account_owner import AccountOwner

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = Account.load_all_accounts()
        self.owners = Owner.load_all_owners()
        self.account_owners = AccountOwner.load_all_account_owners()

    def add_new_account(self, account, owner):
        if existing_account := self.get_account_by_id(account.id):
            print(f"Account with id {account.id} already exists")
            return
        self.accounts.append(account)
        new_ao = AccountOwner(account.id, owner.id)
        self.account_owners.append(new_ao)
        Account.save_account(account)
        AccountOwner.save_account_owner(new_ao)

    def add_new_owner(self, owner):
        if existing_owner := self.get_owner_by_id(owner.id):
            print(f"Owner with id {owner.id} already exists")
            return
        self.owners.append(owner)
        Owner.save_owner(owner)

    def get_account_by_id(self, account_id):
        return next((a for a in self.accounts if a.id == account_id), None)

    def get_owner_by_id(self, owner_id):
        return next((o for o in self.owners if o.id == owner_id), None)

    def withdraw(self, account_id, amount):
        account = self.get_account_by_id(account_id)
        return account and account.withdraw(amount)

    def deposit(self, account_id, amount):
        account = self.get_account_by_id(account_id)
        return account and account.deposit(amount)

    def get_all_owner_accounts(self, owner_id):
        print(self.account_owners)
        account_owners = filter(lambda ao: ao.owner_id == owner_id, self.account_owners)
        return list(map(lambda ao: self.get_account_by_id(ao.account_id), account_owners))