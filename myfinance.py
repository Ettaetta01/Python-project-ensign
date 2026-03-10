def calculate_net_pay():
    wage = float(input("What is your hourly wage? "))
    hours_worked = float(input("How many hours did you work? "))

    gross_pay = wage * hours_worked
    federal_tax = 0.1 * gross_pay
    state_tax = 0.05 * gross_pay
    social_security = 0.062 * gross_pay
    net_pay = gross_pay - (federal_tax + state_tax + social_security)

    print(f"Gross Pay: ${gross_pay:.2f} ({hours_worked} hours @ ${wage:.2f}/hr)")
    print(f"Federal tax: ${federal_tax:.2f}")
    print(f"State tax: ${state_tax:.2f}")
    print(f"Social security: ${social_security:.2f}")
    print(f"Net pay: ${net_pay:.2f}")

def enter_revenue_or_expense():
    transactions = []
    while True:
        transaction_name = input("Enter transaction name: ")
        amount = float(input("Enter amount (use negative sign for expense): "))
        transactions.append((transaction_name, amount))

        another = input("Another? (Y/N): ").lower()
        if another != 'y':
            break

    return transactions

def show_discretionary_income(transactions):
    revenue = 0
    expenses = 0

    for name, amount in transactions:
        if amount < 0:
            expenses += amount
        else:
            revenue += amount

    discretionary_income = revenue + expenses

    print(f"Revenue: ${revenue:.2f} Expenses: ${expenses:.2f} Discretionary: ${discretionary_income:.2f}")

print("1-Calculate net pay")
print("2-Enter revenue or expense")
print("3-Show discretionary income")
print("4-Exit")

while True:
    choice = input("Choice: ")

    if choice == '1':
        calculate_net_pay()
    elif choice == '2':
        transactions = enter_revenue_or_expense()
    elif choice == '3':
        show_discretionary_income(transactions)
    elif choice == '4':
        print("Thanks for using My Finance!")
        break

