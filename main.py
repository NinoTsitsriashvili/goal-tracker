
def reach_goal (current_savings, goal_amount, monthly_amount_rate):
    amount_left = goal_amount - current_savings
    months = amount_left / monthly_amount_rate
    print(months)
    return months
    

def weekly_expenses (monthly_income, monthly_Expenses):
    weekly_allowance = (monthly_income - monthly_Expenses) / 4
    print(weekly_allowance)
    return weekly_allowance


def is_goal_reached ():
    print()





