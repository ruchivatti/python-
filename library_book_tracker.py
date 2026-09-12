books = []

while True:
    print("\n--- Library Book Tracker ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = raw_input("Enter choice: ")

    if choice == "1":
        title = raw_input("Enter book title: ")
        books.append([title, "Available"])
        print("Book added successfully.")

    elif choice == "2":
        if not books:
            print("No books in library.")
        else:
            for i in range(len(books)):
                print(str(i + 1) + ". " + books[i][0] + " - " + books[i][1])

    elif choice == "3":
        title = raw_input("Enter book title to borrow: ")
        found = False

        for book in books:
            if book[0].lower() == title.lower():
                found = True
                if book[1] == "Available":
                    book[1] = "Borrowed"
                    print("Book borrowed.")
                else:
                    print("Book is already borrowed.")

        if not found:
            print("Book not found.")

    elif choice == "4":
        title = raw_input("Enter book title to return: ")
        found = False

        for book in books:
            if book[0].lower() == title.lower():
                found = True
                book[1] = "Available"
                print("Book returned.")

        if not found:
            print("Book not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
