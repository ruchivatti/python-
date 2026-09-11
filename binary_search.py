numbers = [3, 7, 12, 18, 25, 31, 42, 56, 68, 79]

target = int(raw_input("Enter number to search: "))

left = 0
right = len(numbers) - 1
found = False

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Number found at index:", middle)
        found = True
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1

if not found:
    print("Number not found.")
