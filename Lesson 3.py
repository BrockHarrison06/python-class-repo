# Calculate the investment compounded monthly

investment = float(input("Enter investment amount ($1 - $49,999): "))
rate = float(input("Enter yearly interest rate (1% - 14%): "))
years = int(input("Enter investment duration in years: "))

monthly_rate = rate / 100 / 12
total = 0.00

# Calculate the investment compounded monthly
for month in range(1, years * 12 + 1):

    # Add the investment amount
    total += investment

    # Calculate monthly interest
    interest = round(total * monthly_rate, 2)

    # Add the interest to the total
    total += interest

    # Display the investment value at the end of each year
    if month % 12 == 0:
        current_year = month // 12
        print("Year", current_year, "investment value: $", format(total, ".2f"))

# Display final results
monthly_investment = investment

print("\nInvestment duration:", years, "years")
print("Yearly interest rate:", rate, "%")
print("Monthly investment amount: $", format(monthly_investment, ".2f"))
print("Total investment after compounding: $", format(total, ".2f"))

# Completion statement
print("\nCompleted by, Brock Harrison")
