print("--- Attendance Calculator ---")

total_classes = int(raw_input("Enter total classes: "))
attended = int(raw_input("Enter classes attended: "))

if total_classes <= 0:
    print("Total classes must be greater than zero.")
elif attended < 0 or attended > total_classes:
    print("Invalid attendance values.")
else:
    percentage = (attended * 100.0) / total_classes

    print("Attendance:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Status: Eligible")
    else:
        print("Status: Short Attendance")
