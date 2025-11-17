# Planning and Coding

# Project: Creating a python program that help school cafeteria take lunch orders from students and staff.
# The program will display a menu of lunch options, ask for item and quantity, and then calculate the total cost.

# Ways of understanding the problem: 3 Stages of program planning
# 1. Purpose: What wil l the program do?
# The program will help the school cafeteria take lunch orders from students and staff by displaying a menu
# 2. Users: Who will use the program?
# Students and staff at the school will use the program to place their lunch orders.
# 3. Inputs: What information is needed to run the program?
# The program will need the lunch menu items, their prices, and the quantity of each item ordered.
# 4. Process: What steps will the program take to solve the problem?
# The program will display the menu, take orders, calculate the total cost, and provide a summary.

# 5. Outputs: What information will the program provide?
# The program will provide the total cost of the lunch order and a summary of the items ordered

# Algorithm/ Planning (Pseudocode):
# 1. Display menu
# 2. Take order (item) 
# 3. Take quantity
# 4. Calculate total cost
# 5. Display total cost and summary

# Pseudocode Example:
def take_lunch_order():
    # Display menu
    menu = {
        "UNION Sandwich": 5.00,
        "VUU Salad": 4.50,
        "Da Panther Soup": 3.00,
        "Drink": 1.50
    }
    print("Da VUU Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    
    # Take order
    order = {}
    while True:
        item = input("Enter the item you want to order (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        if item in menu:
            quantity = int(input(f"Enter quantity of {item}: "))
            order[item] = order.get(item, 0) + quantity
        else:
            print("Item not on the menu. Please choose again.")
    
    # Calculate total cost
    total_cost = sum(menu[item] * quantity for item, quantity in order.items())
    
    # Display total cost and summary
    print("\nOrder Summary:")
    for item, quantity in order.items():
        print(f"{item} x {quantity} = ${menu[item] * quantity:.2f}")
    print(f"Total Cost: ${total_cost:.2f} Thank you for your order!")

# Optional Extentions: 
# 1. Add tax 6%
# 2. Add more menu items
# 3. Handle invalid inputs
# 4. Print receipt
