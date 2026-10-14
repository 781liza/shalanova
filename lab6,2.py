text = "cat dog cat"
words = text.split()

counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

most_frequent = words[0]
max_count = counts[most_frequent]

for w in counts:
    if counts[w] > max_count:
        max_count = counts[w]
        most_frequent = w

print(most_frequent)
