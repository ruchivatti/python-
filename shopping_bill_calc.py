items = []
total = 0

n = int(raw_input("Enter number of items: "))

for i in range(n):
    name = raw_input("Enter item name: ")
    price = float(raw_input("Enter price: "))
    quantity = int(raw_input("Enter quantity: "))

    cost = price * quantity
    total += cost
    items.append((name, cost))

print("\n----- BILL -----")

for name, cost in items:
    print(name, ":", cost)

print("----------------")
print("Total:", total)
