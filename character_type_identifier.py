ch = raw_input("Enter a character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase letter")
elif ch >= 'A' and ch <= 'Z':
    print("Uppercase letter")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special character")
