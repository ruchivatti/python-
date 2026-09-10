import calendar

year = int(raw_input("Enter year: "))
month = int(raw_input("Enter month (1-12): "))

if month >= 1 and month <= 12:
    print("\n")
    print(calendar.month(year, month))
else:
    print("Invalid month.")
