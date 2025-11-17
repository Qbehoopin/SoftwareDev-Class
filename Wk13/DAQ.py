
# DAQ.py - Simple lunch ordering program

def display_menu(items):
    print("Today's Lunch Menu:")
    for idx, (name, price) in enumerate(items, start=1):
        print(f"  {idx}. {name} - ${price:.2f}")
    print("  C. Checkout")
    print()

def display_cart(cart, items):
    if not cart:
        print("Cart: (empty)\n")
        return
    print("Current cart:")
    subtotal = 0.0
    for idx, qty in cart.items():
        name, price = items[idx]
        line_total = price * qty
        subtotal += line_total
        print(f"  {qty} x {name} @ ${price:.2f} = ${line_total:.2f}")
    print(f"Subtotal: ${subtotal:.2f}\n")

def get_choice_or_checkout(num_items):
    while True:
        choice = input(f"Choose an item by number (1-{num_items}) or 'C' to checkout: ").strip()
        if not choice:
            continue
        if choice.lower() == 'c':
            return 'checkout'
        if not choice.isdigit():
            print("Please enter a valid number or 'C' to checkout.")
            continue
        choice = int(choice)
        if 1 <= choice <= num_items:
            return choice - 1
        print("Choice out of range. Try again.")

def get_quantity():
    while True:
        qty = input("Enter quantity: ").strip()
        if not qty.isdigit():
            print("Please enter a positive whole number.")
            continue
        qty = int(qty)
        if qty > 0:
            return qty
        print("Quantity must be at least 1.")

def main():
    items = [
        ("Turkey & Swiss Sandwich", 7.50),
        ("Caesar Salad", 6.25),
        ("Cheeseburger", 8.00),
        ("Slap Ya Mama Soup", 4.50),
        ("Veggie Wrap", 6.75),
        ("Iced Tea", 2.00)
    ]

    cart = {}  # maps item index -> quantity

    while True:
        display_menu(items)
        display_cart(cart, items)
        choice = get_choice_or_checkout(len(items))
        if choice == 'checkout':
            break
        qty = get_quantity()
        # add to cart (accumulate quantity if item already selected)
        cart[choice] = cart.get(choice, 0) + qty
        name, price = items[choice]
        print(f"Added {qty} x {name} to cart.\n")

    # Checkout summary
    print("\n--- Checkout ---")
    if not cart:
        print("Your cart is empty. Nothing to checkout.")
    else:
        subtotal = 0.0
        for idx, qty in cart.items():
            name, price = items[idx]
            line_total = price * qty
            subtotal += line_total
            print(f"{qty} x {name} @ ${price:.2f} = ${line_total:.2f}")
        print(f"\nTotal: ${subtotal:.2f}")
        print("\nThank you for your order! Have a great meal.")

if __name__ == "__main__":
    main()