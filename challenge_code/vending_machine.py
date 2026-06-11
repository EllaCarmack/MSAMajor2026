# Print vending machine title
# Display the amount due as a variable
# Loop until amount due is 0 or less
# While loop
    # Print amount due
    # Print Insert Coin: (Prompt the user to enter a coin), accepted coins are (1, 5, 10, 25)
    # If statement to check if input is valid
    # Reprompt the user if input is invalid (go to top of loop)
    # If input is valid, subtract coin amount from amount due, update amount due,
    # if amount due is 0 or less, print change owed, if not, reprompt user (go to top of loop)

def main():
    print("\n Vending Machine \n -----------")
    amount_due = 50
    q = 25
    d = 10
    n = 5
    p = 1
    while True:
        print("Amount Due:")
        user_input = input("Insert Coin: ")
        if user_input == "1" or user_input == "5" or user_input == "10" or user_input == "25":
            




main()


