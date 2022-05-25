import csv
import os
from classes.month import Month
from classes.category import Category
from classes.transaction import Transaction


class Budget:
    def __init__(self, monthly_income):
        self.monthly_income = monthly_income
        self.transactions = []

    # Saves new monthly income to csv db
    def set_monthly_income_from_db(self, income):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/monthly_income.csv")
        with open(path, "w") as file:
            writer = csv.writer(file)
            writer.writerow([income])
        self.monthly_income = income

    # Update monthly income with the monthly income in the csv db
    # If there is no monthly income saved in csv db, monthly income defaults to $0
    def get_monthly_income_from_db(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/monthly_income.csv")
        with open(path, "r") as file:
            csv_file = csv.reader(file)
            monthly_income = next(csv_file)
        self.monthly_income = monthly_income[0] if monthly_income else 0

    # Get a new transaction from user. Write it to csv and push it to self.transactions
    def get_transaction(self, transaction):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/expenses.csv")
        with open(path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [transaction.month, transaction.amount, transaction.category]
            )
        self.transactions.append(transaction)

    # Get the total monthly expense amount
    def get_total_monthly_expense_amount(self):
        return sum(int(expense.amount) for expense in self.transactions)

    # Print the percentage of overall expense for each category
    def get_percentage_expense_for_all_categories(self, totals_dict):
        for item in totals_dict:
            cat = Category.get_name_from_value(item)
            percent = self.get_percentage_expense_for_category(item)
            print(f"{cat} {percent}")

    # Get percentage expense for one category
    def get_percentage_expense_for_category(self, category):
        total_expenses = self.get_total_monthly_expense_amount()
        category_expenses = sum(int(expense.amount) for expense in self.transactions if int(expense.category) == category)

        return f"{round((category_expenses / total_expenses) * 100, 1)}%"

    # Get monthly expenses for all categories
    def get_monthly_expense_for_all_categories(self):
        all_percentages = {cat.value: 0 for cat in Category}
        for transaction in self.transactions:
            all_percentages[int(transaction.category)] += int(transaction.amount)
        return all_percentages

    # Get all transactions
    def get_transactions(self):
        self.get_transactions_from_db()
        return self.transactions

    # Update self.transations with transactions from the csv file
    def get_transactions_from_db(self):
        all_transactions = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/expenses.csv")
        with open(path, "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                transaction = Transaction(row["month"], row["amount"], row["category"])
                all_transactions.append(transaction)
        self.transactions = all_transactions

    # Get a list of expenses for one category.
    def get_monthly_expense_list_by_category(self, category):
        return [expense for expense in self.transactions if int(expense.category) == int(category)]