from classes.account import Account
from classes.bank import Bank
from classes.owner import Owner
from classes.savings_account import SavingsAccount

b = Bank("CodePlatoon Bank")

print(b.accounts)
print(b.owners)
print(b.account_owners)

bill = Owner("99", "Gates", "Bill", "123 Riche Ave", "Seattle", "Washington")

a_normal = Account("6666", "10000") # $100.00
a_savings = SavingsAccount("77777", "20000") # $200.00

b.add_new_owner(bill)
b.add_new_account(a_normal, bill)
b.add_new_account(a_savings, bill)

print(b.withdraw(a_normal.id, 8000))
print(b.withdraw(a_savings.id, 8000))

# exceed min balance
print(b.withdraw(a_normal.id, 8000))
print(b.withdraw(a_savings.id, 12000))

print(b.get_all_owner_accounts(bill.id))