sentence = raw_input("Enter a sentence: ")

words = sentence.split()
reversed_words = words[::-1]

print("Reversed sentence:", " ".join(reversed_words))
