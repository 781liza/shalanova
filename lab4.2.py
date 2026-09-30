p = 1

for n in range(1, 21):
    top = (2 * n - 1) ** (n / 3)
    bottom = (2 ** (n + 1)) * (2 * n + 1)
    p *= top / bottom

print("Результат произведения:", p)