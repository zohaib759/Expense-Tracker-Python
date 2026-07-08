import csv
user="zohaib"
password="zohaib123"
attempt=0
for i in range(3):
    user_input=input("Enter Your Username: ")
    password_input=input("Enter Your Password: "
    )
    if user_input==user and password_input==password:
        print("Login Successful!")
        break
    else:
        attempt+=1
        print(f"Login Failed! Attempt {attempt} of 3.")

class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


class ExpenseTracker:
    def __init__(self):
        self.expense = []

    def add_Expense(self):
        date = input("Enter the date of expense in YYYY-MM-DD format: ")
        category = input("Enter the category of expense: ")
        amount = float(input("Enter the amount of expense: "))
        description = input("Enter the description of expense: ")

        expense = Expense(amount, category, date, description)
        self.expense.append(expense)

        print("Expense added successfully!")

    def view_Expenses(self):
        if not self.expense:
            print("No Expense Found...")
        else:
            print("\nExpenses:")
            for e in self.expense:
                print(f"Date: {e.date}, Category: {e.category}, Amount: {e.amount}, Description: {e.description}")

    def monthly_Report(self):
        if not self.expense:
            print("No Expense Found....")
        else:
            month = input("Enter The Month in YYYY-MM format: ")
            total = 0
            print(f"\nExpenses for {month}:")
            for e in self.expense:
                if e.date.startswith(month):
                    print(f"Date: {e.date}, Category: {e.category}, Amount: {e.amount}, Description: {e.description}")
                    total += e.amount
            print(f"\nTotal Expenses for {month}: {total}")

    def category_report(self):
        if not self.expense:
            print("No Expense Found....")
        else:
            category = input("Enter the category for report: ")
            total = 0
            print(f"\nExpenses for category '{category}':")
            for e in self.expense:
                if e.category.lower() == category.lower():
                    print(f"Date: {e.date}, Category: {e.category}, Amount: {e.amount}, Description: {e.description}")
                    total += e.amount
            print(f"\nTotal Expenses for category '{category}': {total}")

    def budget_alert(self):
        if not self.expense:
            print("No Expense Found....")
        else:
            budget = float(input("Enter your budget amount: "))
            total = 0
            for e in self.expense:
                total += e.amount

            if total > budget:
                print(f"Alert! You have exceeded your budget of {budget}. Total expenses: {total}")
            else:
                print(f"You are within your budget of {budget}. Total expenses: {total}")

    def export_csv(self):
        if not self.expense:
            print("No Expense Found....")
        else:
            filename = input("Enter the filename to export (with .csv extension): ")

            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Category", "Amount", "Description"])

                for e in self.expense:
                    writer.writerow([e.date, e.category, e.amount, e.description])

            print(f"Expenses exported to {filename} successfully!")


tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Generate Monthly Report")
    print("4. Generate Category Report")
    print("5. Check Budget Alert")
    print("6. Export to CSV")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        tracker.add_Expense()

    elif choice == 2:
        tracker.view_Expenses()

    elif choice == 3:
        tracker.monthly_Report()

    elif choice == 4:
        tracker.category_report()

    elif choice == 5:
        tracker.budget_alert()

    elif choice == 6:
        tracker.export_csv()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")