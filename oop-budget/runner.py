# After you write all your classes, use this file to call them all together and run your program
import sys
from classes.budget import Budget
from classes.category import Category
from classes.transaction import Transaction

def main():  # sourcery skip: avoid-builtin-shadow
    budget = Budget(0)
    budget.get_transactions_from_db()
    budget.get_monthly_income_from_db()
    message = "\nWhat would you like to do?\n1. Update Monthly Income.\n2. View Current Monthly Income.\n3. See Expenses Per Category.\n4. Add New Expense.\n5. See Monthly Summary by Category.\n6. Exit.\n\nInput: "
    while True:
        input_selection = int(input(message))
        if input_selection == 6:
            sys.exit()
        elif input_selection == 1:
            new_income = int(input("Enter new income: "))
            budget.set_monthly_income_from_db(new_income)
            print(f"Your monthly income has been updated to ${budget.monthly_income}!")
        elif input_selection == 2:
            print(f"Your current monthly income is ${budget.monthly_income}.")
        elif input_selection == 3:
            category = int(
                input(
                    "Which Category Would you like to see?\n1. Food\n2. Living\n3. Travel\n\nInput: "
                )
            )
            expense_for_category = budget.get_percentage_expense_for_category(category)
            cat = Category.get_name_from_value(category)
            print(f"\nOverall expense percentage for {cat}: {expense_for_category}.\n")
            list = budget.get_monthly_expense_list_by_category(category)
            i = 1
            for i, item in enumerate(list, 1):
                print(f"{i}. Expense Amount: ${item.amount}")
            main_menu = input("\nEnter 1 to return to main menu or q to quit: ")
            if main_menu == "q":
                sys.exit()
        elif input_selection == 4:
            print(
                "Transaction Category:\nEnter 1 for Food\nEnter 2 for Living\nEnter 3 for Travel "
            )
            transaction_category = input("Enter Tansaction Category: ")
            print(
                "Transaction Month:\nEnter 1 for JAN\nEnter 2 for FEB\nEnter 3 for MAR\nEnter 4 for APR\nEnter 5 for MAY\nEnter 6 for JUN\nEnter 7 for JUL\nEnter 8 for AUG\nEnter 9 for SEP\nEnter 10 for OCT\nEnter 11 for NOV\nEnter 12 for DEC"
            )
            transaction_month = input("Enter Tansaction Month: ")
            print("Transaction Amount: ")
            transaction_amount = input("Enter Tansaction Amount: ")

            new_transaction = Transaction(
                transaction_month, transaction_amount, transaction_category
            )
            budget.get_transaction(new_transaction)
        elif input_selection == 5:
            expenses_dict = budget.get_monthly_expense_for_all_categories()
            print("\nExpense Percentages by Category:")
            budget.get_percentage_expense_for_all_categories(expenses_dict)

main()