isbn = raw_input("Enter a 10-digit ISBN: ")

if len(isbn) != 10:
    print("Invalid ISBN length.")
else:
    total = 0
    valid = True

    for i in range(10):
        ch = isbn[i]

        if i == 9 and ch.upper() == 'X':
            value = 10
        elif ch.isdigit():
            value = int(ch)
        else:
            valid = False
            break

        total += (10 - i) * value

    if valid and total % 11 == 0:
        print("Valid ISBN-10")
    else:
        print("Invalid ISBN-10")
