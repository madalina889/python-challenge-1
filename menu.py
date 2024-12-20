# Menu dictionary 
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
 
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered


order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
    #print(menu_items)    
    #'Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
    
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number?
            menu_selection = input( "Enter the item you would like")
            
            # 3. Check if the customer typed a number

            if menu_selection.isdigit():
        
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():

                    # Store the item name as a variable
                    item_name_name = menu_items[menu_selection]['Item name']
                    menu_item_price = menu_items[menu_selection]['Price']

                    # Ask the customer for the quantity of the menu item
                    item_quantity = input("Enter the quantity of the items you need from the menu ")
                    
                    # Check if the quantity is a number, default to 1 if not
                    if item_quantity.isdigit():
                        item_quantity = int(item_quantity)
                    else :
                        item_quantity = 1   

                    # Add the item name, price, and quantity to the order list
                
                else:
                    print("Your selectio is not valid. ")

                order_dict = {"item name": menu_category_name, "Price": menu_item_price, "Quantity":item_quantity}

                

                    # Tell the customer that their input isn't valid
            else: 
                print("Your selection si not valid .")

                    # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (y)es or (n)o ")

        # 5. Check the customer's input
        match keep_ordering: 
            case 'y':
                # Keep ordering 
                 print("Great, Let's add more items to your order .")
                 break
            
                # Complete the order
            case 'n':
                print("Thanks for your order.")
                # Since the customer decided to stop ordering, thank them for
                # their order
                place_order = False
                break
                # Exit the keep ordering question loop
                
            
            # Customer typed an invalid input 
            case _:
                # Tell the customer to try again
                print("I didn't understand your response. Please try again.")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
grand_total = 0
for order_item in order_list :
    
    # 7. Store the dictionary items as variables
    menu_category_name = order_item[" Item name"]
    menu_category_price = order_item["price"]
    item_quantity = order_item["quantity"]
    order_dict = menu_item_price * item_quantity

    grand_total += order_dict

    # 8. Calculate the number of spaces for formatted printing
    spaces_needed = item_quantity - len(menu_category_name)

    # 9. Create space strings
    item_spaces = " " * 24
    price_spaces = " " * 7
    name_spaces = " " * (24 - len(menu_category_name))
    price_spaces = " " * (6 - len(f"{menu_category_price:.2f}"))
    quantity_spaces = " " * (8 - len(str(item_quantity)))

    # 10. Print the item name, price, and quantity
    print(f"{menu_category_name}{name_spaces} | ${menu_category_price:.2f}{price_spaces} | {item_quantity}{quantity_spaces} | ${order_dict:.2f}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum([item["price"] * item["quantity"] for item in order_list])
print(f"Total cost of the order: ${total_cost:.2f}")

print("--------------------------|--------|----------|------------")
print(f"Grand Total:{' ' * 15} | ${grand_total:.2f}")