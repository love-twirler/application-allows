# main.py
from item import Item
from inventory import Inventory

def get_numeric_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_inventory(inventory):
    print("\nInventory:")
    items = inventory.get_items()
    if not items:
        print("No items in the inventory.")
    else:
        for item in items:
            print(f"{item.name} - ${item.price}")

def main():
    inventory = Inventory()

    while True:
        print("\nMenu:\n1. Add Item\n2. View Inventory\n3. Exit")
        choice = get_numeric_input("Enter your choice: ")

        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            new_item = Item(item_name, item_price)
            inventory.add_item(new_item)
            print("Item added to inventory.")
        elif choice == 2:
            display_inventory(inventory)
        elif choice == 3:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
