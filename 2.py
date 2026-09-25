import math
print("Задание 2")
a = -0.7
b = 0.7
step = 0.05
steps_count = int((b-a) / step )+1
for i in range(steps_count):
    x = a+i *step
    y = ((1+x)**(1+x))/((1 - x)**(1-x))
    print ("x=", round (x , 2), "y =", round(y, 5))