import random

rolls = int(raw_input("Enter number of rolls: "))

results = [0] * 6

for i in range(rolls):
    value = random.randint(1, 6)
    results[value - 1] += 1

print("\nDice Statistics:")

for i in range(6):
    print("Side", i + 1, ":", results[i], "times")
