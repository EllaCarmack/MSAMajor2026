# Create main function
def main():
# Display total cost of all items inside a dictionary, with $, format to 2 decimal places
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}

    total = 0
# While Loop
    while True:
        # Prompt the user for an item "Item :"
        user_input = input("Item:\n").title()

        # End when user types a form of "end"
        # Check if input is in Title Case
        if user_input.lower() == "end":
            break
    
        # Check if input is in dictionary, if not then ignore + reprompt user
        if user_input not in menu.keys():
            continue

        # If all checks are correct then update the total and print it
        total = total + menu[user_input]
        print(f"Total: ${total:.2f}")
        
main ()