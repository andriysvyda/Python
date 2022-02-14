import random
import math


n = int(input("n= "))
b = [1, 7, 7, 7]
d = 4
x = 1
for i in range(3, n):
    c = (b[d - 1] * (4*b[d-2])*(1+b[d-2])+ b[d - 3])
    g = math.sqrt(b[d - 4])
    x = c / g
    b = b + [x]
    d += 1
print("xn= {0:.2f}".format(b[n]))