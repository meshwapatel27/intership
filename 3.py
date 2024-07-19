
# Define an empty inventory dictionary
inventory = {}

# Function to add items to inventory
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} {item}(s) to inventory.")

# Function to remove items from inventory
def remove_item(item, quantity):
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
            print(f"Removed {quantity} {item}(s) from inventory.")
        else:
            print(f"Not enough {item} in inventory.")
    else:
        print(f"{item} not found in inventory.")

# Function to display current inventory
def display_inventory():
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Main program loop
while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Inventory")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter item name to add: ")
        quantity = int(input("Enter quantity to add: "))
        add_item(item, quantity)
    elif choice == '2':
        item = input("Enter item name to remove: ")
        quantity = int(input("Enter quantity to remove: "))
        remove_item(item, quantity)
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
