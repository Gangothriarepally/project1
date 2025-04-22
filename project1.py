import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

FILE = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    
    with open(FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])
    print("✅ Expense added!")

def view_expenses():
    if not os.path.exists(FILE):
        print("No expenses yet!")
        return
    
    with open(FILE, 'r') as f:
        reader = csv.reader(f)
        print(f"\n{'Date':<12} {'Category':<10} {'Amount':<8}")
        print("-" * 35)
        for row in reader:
            print(f"{row[0]:<12} {row[1]:<10} ₹{row[2]:<8}")

def plot_expenses():
    if not os.path.exists(FILE):
        print("No data to plot.")
        return

    category_totals = {}
    with open(FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            category_totals[category] = category_totals.get(category, 0) + amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Distribution')
    plt.axis('equal')
    plt.show()

def main():
    while True:
        print("\n🔸 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expense Chart")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            plot_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
