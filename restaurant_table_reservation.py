tables = {
    1: "Available",
    2: "Available",
    3: "Available",
    4: "Available",
    5: "Available"
}

while True:
    print("\n--- Restaurant Table Reservation ---")
    print("1. View Tables")
    print("2. Reserve Table")
    print("3. Cancel Reservation")
    print("4. Exit")

    choice = raw_input("Enter choice: ")

    if choice == "1":
        for table in tables:
            print("Table", table, "-", tables[table])

    elif choice == "2":
        table = int(raw_input("Enter table number: "))

        if table not in tables:
            print("Invalid table number.")
        elif tables[table] == "Reserved":
            print("Table is already reserved.")
        else:
            tables[table] = "Reserved"
            print("Table reserved successfully.")

    elif choice == "3":
        table = int(raw_input("Enter table number: "))

        if table not in tables:
            print("Invalid table number.")
        elif tables[table] == "Available":
            print("Table is not reserved.")
        else:
            tables[table] = "Available"
            print("Reservation cancelled.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
