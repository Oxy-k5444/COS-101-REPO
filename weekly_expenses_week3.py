# This program calculates a student's weekly expenses
# and compares the total expenses with the weekly budget.

# Get expense details from the user
daily_transport = int(input("Enter your daily transport expense: "))
daily_feeding = int(input("Enter your daily feeding expense: "))
number_of_days = int(input("Enter the number of days: "))
other_expenses = int(input("Enter your other weekly expenses: "))
weekly_budget = int(input("Enter your weekly budget: "))

# Check that none of the values is negative
if daily_transport < 0 or daily_feeding < 0 or number_of_days < 0 or other_expenses < 0 or weekly_budget < 0:
    print("Invalid input. Negative values are not allowed.")

else:
    # Calculate the total transport and feeding expenses
    total_transport = daily_transport * number_of_days
    total_feeding = daily_feeding * number_of_days

    # Calculate the total weekly expenses
    total_expenses = total_transport + total_feeding + other_expenses

    # Display the expense details
    print("Total transport expenses:", total_transport)
    print("Total feeding expenses:", total_feeding)
    print("Other weekly expenses:", other_expenses)
    print("Total weekly expenses:", total_expenses)
    print("Weekly budget:", weekly_budget)

    # Compare the total expenses with the weekly budget
    if total_expenses < weekly_budget:
        amount_remaining = weekly_budget - total_expenses
        print("Within budget")
        print("Amount remaining:", amount_remaining)

    elif total_expenses == weekly_budget:
        print("Exactly on budget")
        print("Amount remaining: 0")

    else:
        amount_exceeded = total_expenses - weekly_budget
        print("Over budget")
        print("Amount exceeded:", amount_exceeded)

# TEST CASES
#
# Test 1 - Within budget:
# Daily transport = 500, daily feeding = 1000, days = 5,
# other expenses = 1000, budget = 10000.
# Total expenses = 8500. Expected result: Within budget,
# amount remaining = 1500.
#
# Test 2 - Exactly on budget:
# Daily transport = 500, daily feeding = 1000, days = 5,
# other expenses = 2500, budget = 10000.
# Total expenses = 10000. Expected result: Exactly on budget.
#
# Test 3 - Over budget:
# Daily transport = 500, daily feeding = 1000, days = 5,
# other expenses = 4000, budget = 10000.
# Total expenses = 11500. Expected result: Over budget,
# amount exceeded = 1500.
#
# Test 4 - Invalid value:
# Daily transport = -500, daily feeding = 1000, days = 5,
# other expenses = 1000, budget = 10000.
# Expected result: Invalid input. Negative values are not allowed.
