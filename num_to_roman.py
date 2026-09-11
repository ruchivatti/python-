n = int(raw_input("Enter a number (1-3999): "))

values = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

if n < 1 or n > 3999:
    print("Number must be between 1 and 3999.")
else:
    result = ""

    for value, symbol in values:
        while n >= value:
            result += symbol
            n -= value

    print("Roman numeral:", result)
