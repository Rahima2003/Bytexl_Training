def add_expense(transactions, date, category, amount, description):
    """
    Add a new expense to the transactions list.
    """
    transaction = (date, category, amount, description)
    transactions.append(transaction)
    print("Expense added successfully!")

def view_expenses_by_category(transactions, category):
    """
    View expenses by a specific category.
    """
    filtered_transactions = [t for t in transactions if t[1] == category]
    if filtered_transactions:
        print(f"Expenses for category '{category}':")
        for t in filtered_transactions:
            print(f"Date: {t[0]}, Amount: {t[2]}, Description: {t[3]}")
    else:
        print(f"No expenses found for category '{category}'.")

def calculate_total_expenditure(transactions, start_date, end_date):
    """
    Calculate total expenditure over a specified period.
    """
    total = 0
    for t in transactions:
        if start_date <= t[0] <= end_date:
            total += t[2]
    return total

def main():
    transactions = []

    while True:
        print("\nExpense Tracker")
        print("1. Add New Expense")
        print("2. View Expenses by Category")
        print("3. Calculate Total Expenditure")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(transactions, date, category, amount, description)
        elif choice == '2':
            category = input("Enter category to view expenses: ")
            view_expenses_by_category(transactions, category)
        elif choice == '3':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            total = calculate_total_expenditure(transactions, start_date, end_date)
            print(f"Total expenditure from {start_date} to {end_date}: {total}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
