contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Show Contacts")
    print("4. Exit")

    choice = raw_input("Enter choice: ")

    if choice == "1":
        name = raw_input("Enter name: ")
        phone = raw_input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == "2":
        name = raw_input("Enter name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        for name in contacts:
            print(name, ":", contacts[name])

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
