rows = int(raw_input("Enter number of rows: "))
cols = int(raw_input("Enter number of columns: "))

a = []
b = []

print("Enter first matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(raw_input("Enter value: ")))
    a.append(row)

print("Enter second matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(raw_input("Enter value: ")))
    b.append(row)

result = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(a[i][j] + b[i][j])
    result.append(row)

print("\nResult Matrix:")

for row in result:
    print(row)
