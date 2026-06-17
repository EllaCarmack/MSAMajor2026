# Function to load data from a file and return a dictionary
# Input: filename: string
# Output: dictionary
def load_menu_items(filename:str) -> dict:
    # open menu.txt: create a file handler to open file in read mode
    data_file = open(filename, "r")
    
    # create an empty dictonary
    menu_items = {}
    # use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        # split the line at the comma
        item_name_and_price = line_of_data.split(",")

        # get the item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        # create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price

    # close the file
    data_file.close()

    # return the dictinary of menu items
    return menu_items


def main():
# Display total cost of all items inside a dictionary, with $, format to 2 decimal places
    menu = load_menu_items("menu.txt")

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