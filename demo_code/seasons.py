# Create a decision structure to determine the season:
# Winter, Spring, Summer, Fall
# Ask the user to enter the number of the month. Month must be 1 - 12
# winter: 12, 1, 2 | spring: 3, 4, 5 | summer: 6, 7, 8 | fall: 9, 10, 11
# Output the season
# Enter month number: 11
# Output: It is Fall

# prompt the user
def get_month():
    while True:
        try:
            month = int(input("Enter the number of a month: "))
            # if month is less than or equal to 0, give error message
            if month <= 0 or month > 12:
                print("ERROR: Enter a number greater than 0. \n")
                continue
            break
        except:
            print("ERROR: Please enter a number.\n")
            continue
    
    return month

def main():
    month = get_month()
    if month == 12 or month == 1 or month == 2:
        print("It is Winter")
    elif month == 3 or month == 4 or month == 5:
        print("It is Spring")
    elif month == 6 or month == 7 or month == 8:
        print("It is Summer")
    elif month == 9 or month == 10 or month == 11:
        print("It is Fall")

main()