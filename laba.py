import math
print("Задание 1")
x=0.5
y1 =(math.acos(1-x**2)+math.asin(1-x**2))/math.sin(1 - 2 * x**2)
print("y =" , round(y1, 5))