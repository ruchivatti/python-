start = int(raw_input("Enter starting number: "))
end = int(raw_input("Enter ending number: "))

even = 0
odd = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
