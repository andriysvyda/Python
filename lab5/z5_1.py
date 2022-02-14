n = int(input("кількість ітерацій : "))
a = int(input("введіть число : "))
b = 2
suma = 0
for i in range(n):
    a *= a+1
    b *= 2
    suma += b/a
print("сума = {0:.2f}".format(suma))
