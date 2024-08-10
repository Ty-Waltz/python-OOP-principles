class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.__name = name
        self.__allocated_budget = allocated_budget

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, budget):
        if budget >= 0:
            self.__allocated_budget = budget
        else:
            raise ValueError("Budget cannot be negative.")

    def add_expense(self, amount):
        if amount >= 0:
            if amount <= self.__allocated_budget:
                self.__allocated_budget -= amount
            else:
                raise ValueError("Expense is more than the budget.")
        else:
            raise ValueError("Expense amount cannot be negative.")

    def display_category_summary(self):
        print(f"Category: {self.__name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
