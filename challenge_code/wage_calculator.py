def get_daily_hours():
    while True:
        # Prompt user to input hours worked daily hourly wage. Multiply hours daily and hourly wage will give you the wages earned in a day.
        try:
            # The two input numbers don't have to be integers, the user can enter floats.
            daily_hours = float(input("Enter the number of hours worked daily: "))
            # the user can't work more than 24 hours in a day
            if daily_hours > 24 or daily_hours <= 0:
                print("ERROR: Enter a number less than 24 and greater than 0. \n")
                continue
            break
        except:
            print("ERROR: Please enter a number.\n")
            continue
    return daily_hours

def get_hourly_wage():
    while True:
        try:
            hourly_wage = float(input("Enter the hourly wage: "))
            if hourly_wage <= 0:
                print("ERROR: Enter a number greater than 0. \n")
                continue
            break
        except:
            print("ERROR: Please enter a number.\n")
            continue
    return hourly_wage
        
# Print the Pay Advice to include, hours worked, hourly wage, calculated yearly wage, wages before taxes, 12% tax deduction from yearly earnings, tax amount, & annual wages after taxes
def main():
    daily_hours = get_daily_hours()
    hourly_wage = get_hourly_wage()
    print("\nPay Advice\n----------")
    print(f"Daily Hours: {daily_hours:.2f} ")
    print(f"Hourly Wage: ${daily_hours:.2f} ")
    daily_wages = daily_hours * hourly_wage
    # Note that the working hours is daily. Assume the user works 350 days per year and the same amount of hours every day.
    yearly_wages = daily_wages * 350
    print(f"Wages Before Taxes: ${yearly_wages:.2f} ")
    tax_amount = yearly_wages * 0.12
    print(f"Tax Amount: ${tax_amount:.2f} ")
    annual_wage_after_tax = yearly_wages - tax_amount
    print(f"Annual Wages After Tax: ${annual_wage_after_tax:.2f} ")
main()