
income = input("Enter your monthly income:")
expenses = input("Enter your total monthly expenses:")
monthly_income = int(income)
total_monthly_expenses = int(expenses)
monthly_savings = monthly_income - total_monthly_expenses
yearly_savings = monthly_savings * 12
interest =  yearly_savings * 0.05
projected_savings = yearly_savings + interest
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")

