text = raw_input("Enter text: ")
shift = int(raw_input("Enter shift: "))

result = ""

for ch in text:
    if ch >= 'a' and ch <= 'z':
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    elif ch >= 'A' and ch <= 'Z':
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    else:
        result += ch

print("Encrypted text:", result)
