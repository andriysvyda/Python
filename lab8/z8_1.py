import math

def kvadratrivn1():
    print("Введіть числа для виразу")
    print("ax**2 + bx + c = 0:") # Формула
    a = float(input("a = "))
    b = 2
    c = 7

    discr = b ** 2 - 4 * a * c
    print("Дискримінант D = %.2f" % discr)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Коренів немає")
def kvadratrivn2():
    print("Введіть числа для виразу")
    print("bx**2 + ax + c = 0:") # Формула
    b = float(input("b = "))
    a = 5
    c = 2

    discr = a ** 2 - 4 * b * c
    print("Дискримінант D = %.2f" % discr)

    if discr > 0:
        x1 = (-a + math.sqrt(discr)) / (2 * b)
        x2 = (-a - math.sqrt(discr)) / (2 * b)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -a / (2 * b)
        print("x = %.2f" % x)
    else:
        print("Коренів немає")
print(kvadratrivn1())
print(kvadratrivn2())