slots = [False] * 10

while True:
    print("\n1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Show Slots")
    print("4. Exit")

    choice = raw_input("Enter choice: ")

    if choice == "1":
        slot = int(raw_input("Enter slot number (1-10): "))

        if slot < 1 or slot > 10:
            print("Invalid slot.")
        elif slots[slot - 1]:
            print("Slot already occupied.")
        else:
            slots[slot - 1] = True
            print("Vehicle parked in slot", slot)

    elif choice == "2":
        slot = int(raw_input("Enter slot number (1-10): "))

        if slot < 1 or slot > 10:
            print("Invalid slot.")
        elif not slots[slot - 1]:
            print("Slot is already empty.")
        else:
            slots[slot - 1] = False
            print("Vehicle removed.")

    elif choice == "3":
        print("\nParking Slots:")

        for i in range(10):
            if slots[i]:
                print("Slot", i + 1, ": Occupied")
            else:
                print("Slot", i + 1, ": Empty")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
