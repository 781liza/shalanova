text = "cat dog cat"
words = text.split()
most_frequent = max(words, key=words.count)
print(most_frequent)