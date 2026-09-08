hours = int(raw_input("Enter parking hours: "))

if hours <= 2:
    fee = 20
else:
    fee = 20 + (hours - 2) * 10

print("Parking Fee:", fee)
