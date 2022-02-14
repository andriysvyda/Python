n = int(input("Введіть довжину масиву : "))
a = []
suma = 0
s = 1
for i in range(1,n+1) :
    s *= ((-1)**i)*i
    a.append(s/n)
    if a[i - 1] > 0:
        suma += a[i - 1]
    print(a)
print("сума = {0}".format(suma))