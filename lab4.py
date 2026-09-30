from math import*
s = 0
for n in range(1, 51):
    p=(sin((n*pi)/2))/(2*n**n+factorial(n))
    s=s+p
print(s)