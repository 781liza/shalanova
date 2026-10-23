a = [3, 1, 2, 3, 1, 2, 5]
best = a[0]
best_count = a.count(a[0])
for x in a:
    c = a.count(x)
    if c > best_count:
        best = x 
        best_count = c 
    elif c == best_count and x < best:
            best = x
print(best)