# This program calculates a student's weekly expenses.

# Get the required information from the user
daily_transport = float(input("Enter your daily transport expense: "))
daily_feeding = float(input("Enter your daily feeding expense: "))
number_of_days = int(input("Enter the number of days: "))
other_expenses = float(input("Enter your other weekly expenses: "))

# Calculate the total transport and feeding expenses
total_transport = daily_transport * number_of_days
total_feeding = daily_feeding * number_of_days

# Calculate the total weekly expenses
total_expenses = total_transport + total_feeding + other_expenses

# Display the expense details
print("Total transport expenses:", format(total_transport, ",.2f"))
print("Total feeding expenses:", format(total_feeding, ",.2f"))
print("Other weekly expenses:", format(other_expenses, ",.2f"))
print("Total weekly expenses:", format(total_expenses, ",.2f"))
