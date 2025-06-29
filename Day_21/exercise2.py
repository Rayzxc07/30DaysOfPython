class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}
    
    def add_income(self, description, amount):
        """Add an income with description and amount"""
        self.incomes[description] = amount
    
    def add_expense(self, description, amount):
        """Add an expense with description and amount"""
        self.expenses[description] = amount
    
    def total_income(self):
        """Calculate total income"""
        return sum(self.incomes.values())
    
    def total_expense(self):
        """Calculate total expenses"""
        return sum(self.expenses.values())
    
    def account_balance(self):
        """Calculate account balance (total income - total expenses)"""
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        """Return account information as a formatted string"""
        info = f"Account Information for {self.firstname} {self.lastname}\n"
        info += "="*40 + "\n"
        info += "Incomes:\n"
        for desc, amount in self.incomes.items():
            info += f"- {desc}: ${amount:.2f}\n"
        info += "\nExpenses:\n"
        for desc, amount in self.expenses.items():
            info += f"- {desc}: ${amount:.2f}\n"
        info += "\nSummary:\n"
        info += f"Total Income: ${self.total_income():.2f}\n"
        info += f"Total Expenses: ${self.total_expense():.2f}\n"
        info += f"Account Balance: ${self.account_balance():.2f}\n"
        return info
person = PersonAccount("Raymart", "Garcia")
person.add_income("Salary", 5000)
person.add_income("Freelance Work", 1200)
person.add_income("Investments", 300)

person.add_expense("Rent", 1500)
person.add_expense("Groceries", 400)
person.add_expense("Utilities", 200)
person.add_expense("Entertainment", 150)

print(person.account_info())

print(f"\nTotal Income: ${person.total_income():.2f}")
print(f"Total Expenses: ${person.total_expense():.2f}")
print(f"Account Balance: ${person.account_balance():.2f}")