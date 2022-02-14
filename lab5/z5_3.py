import math
import random
x = random.randint(-10,10)
n = int(input("кількість чисел = "))
eps = 0.00001
a = 1
b = math.pi
s = math.cos(x)
dob = x
if abs(dob) > eps:
    for i in range(1, n):
        dob = dob * (1 - ((4*x**2) / ((2*i - 1)**2 * (b ** 2))))
    if s == dob:
        print("Рівність справедлива")
    else:
        print("Не справедлива")
