text = raw_input("Enter a sentence: ")

words = text.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequency:")

for word in frequency:
    print(word, ":", frequency[word])
