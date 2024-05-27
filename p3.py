import json
from datetime import datetime

# Global variables
expenses = []
data_file = 'expenses.json'
categories = ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Other']
def add_expense():
    try:
        amount = float(input("Enter amount spent: "))
        description = input("Enter a brief description: ")
        print("Select a category:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        category_choice = int(input("Enter the category number: "))
        
        if 1 <= category_choice <= len(categories):
            category = categories[category_choice - 1]
        else:
            raise ValueError("Invalid category choice")
        
        expense = {
            'amount': amount,
            'description': description,
            'category': category,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        expenses.append(expense)
        print("Expense added successfully.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def load_expenses():
    try:
        with open(data_file, 'r') as file:
            global expenses
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    except json.JSONDecodeError:
        print("Error reading data file. Starting with an empty list.")
        expenses = []

def save_expenses():
    try:
        with open(data_file, 'w') as file:
            json.dump(expenses, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving expenses: {e}")
def view_expenses():
    if not expenses:
        print("No expenses to show.")
        return
    for expense in expenses:
        print(f"{expense['date']} - {expense['description']} - ${expense['amount']} ({expense['category']})")

def monthly_summary():
    summary = {}
    for expense in expenses:
        month = expense['date'][:7]  # 'YYYY-MM'
        if month not in summary:
            summary[month] = 0
        summary[month] += expense['amount']
    
    print("Monthly Summary:")
    for month, total in summary.items():
        print(f"{month}: ${total:.2f}")

def category_summary():
    summary = {category: 0 for category in categories}
    for expense in expenses:
        summary[expense['category']] += expense['amount']
    
    print("Category Summary:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")
def main():
    load_expenses()
    
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
