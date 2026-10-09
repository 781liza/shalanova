n = int(input())
if n > 0: 
    numbers = [int(input()) for _ in range(n)] 
    max_product = numbers[0] * 1 
    min_sum = numbers[0] + 1
for i in range(n):
    pos = i + 1
    product = numbers[i] * pos
    sum_val = numbers[i] + pos

    if product > max_product:
        max_product = product
    if sum_val < min_sum:
        min_sum = sum_val

print(max_product)
print(min_sum)