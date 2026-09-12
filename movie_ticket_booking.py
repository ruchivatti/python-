print("--- Movie Ticket Booking ---")

movie = raw_input("Enter movie name: ")
tickets = int(raw_input("Enter number of tickets: "))

price = 180
total = tickets * price

if tickets >= 5:
    discount = total * 0.10
    total = total - discount
else:
    discount = 0

print("\n--- Ticket Summary ---")
print("Movie:", movie)
print("Tickets:", tickets)
print("Ticket Price: Rs.", price)
print("Discount: Rs.", discount)
print("Total Amount: Rs.", total)
