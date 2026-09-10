import random

n = int(raw_input("How many dice do you want to roll? "))

total = 0

print("\nResults:")

for i in range(n):
    value = random.randint(1, 6)
    print("Die", i + 1, ":", value)
    total += value

print("Total:", total)
