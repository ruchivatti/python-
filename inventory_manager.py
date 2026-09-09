inventory = {}

while True:
    print("\n1. Add Item")
    print("2. Update Stock")
    print("3. View Inventory")
    print("4. Exit")

    choice = raw_input("Enter choice: ")

    if choice == "1":
        item = raw_input("Enter item name: ")
        quantity = int(raw_input("Enter quantity: "))

        inventory[item] = inventory.get(item, 0) + quantity
        print("Item added.")

    elif choice == "2":
        item = raw_input("Enter item name: ")

        if item in inventory:
            quantity = int(raw_input("Enter new quantity: "))
            inventory[item] = quantity
            print("Stock updated.")
        else:
            print("Item not found.")

    elif choice == "3":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nInventory:")
            for item in inventory:
                print(item, ":", inventory[item])

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
