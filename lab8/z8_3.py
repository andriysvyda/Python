import random
n = int(input("n= "))
x = [0, 7, 7]
def el(x, n):
    for i in range(3, n):
        b = x[i-1] *(1 + x[i-2])
        x = x + [b]
    return(x)
x = el(x, n)
print("x[n]= {0}".format(x[n-1]))