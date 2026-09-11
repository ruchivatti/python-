password = raw_input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch >= 'A' and ch <= 'Z':
        has_upper = True
    elif ch >= 'a' and ch <= 'z':
        has_lower = True
    elif ch >= '0' and ch <= '9':
        has_digit = True
    else:
        has_special = True

score = 0

if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

if score <= 2:
    print("Password strength: Weak")
elif score <= 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")
