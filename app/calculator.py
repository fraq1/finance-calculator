def add_income(balance: float, amount: float) -> float:
    if amount < 0:
        raise ValueError("Income cannot be negative")

    return balance + amount


def add_expense(balance: float, amount: float) -> float:
    if amount < 0:
        raise ValueError("Expense cannot be negative")

    return balance - amount


def calculate_balance(incomes: list[float], expenses: list[float]) -> float:
    if any(income < 0 for income in incomes):
        raise ValueError("Income cannot be negative")

    if any(expense < 0 for expense in expenses):
        raise ValueError("Expense cannot be negative")

    return sum(incomes) - sum(expenses)
