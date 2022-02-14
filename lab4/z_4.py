# y = ye**x, якщо y<x; y*x, якщо y=x; x*e**y, якщо y>x; 4
x = float(input("введiть x: "))
y = float(input("введiть y: "))
e = 2.71828
if y < x:
    z = y*e**x
elif y == x:
    z = y*x
elif  y>x:
    z = x*e**y
print("z = {0:.2f} ".format(z))
