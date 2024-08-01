import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add(self):
        date = input("enter the date (YYYY-MM-DD): ")
        description = input("enter the description: ")
        amount = input("enter the amount: ")

        expense = {'date': date, 'description': description, 'amount': amount}
        self.expenses.append(expense)

        print("*****expense added successfully!*****")
        # date = date(input("enter the date: "))
        # expense = {'date': date}
        # self.expenses.append(expense)
        # print(date)

    def view(self):
        print("\n Date \t\t Description \t\t Amount")
        for expense in self.expenses:
            print("-------------------------------------------------------------")
            print(f"{expense['date']}\t{expense['description']}\t\t\t{expense['amount']}")

            # print("\n")

# tracker = ExpenseTracker(date)
# tracker.add()
tracker = ExpenseTracker()


while True:
    print("-------------------------------------------------------------")
    print("my expenses:")
    print("-------------------------------------------------------------")
    print("1. add expense")
    print("2. view expense")
    print("3. exit")
    print("-------------------------------------------------------------")


    choice = input("enter your choice: ")
    
    if choice == '1':
        tracker.add()
    elif choice == '2':
        tracker.view()
    elif choice == '3':
        break
    else:
        print("invalid choice. ")
