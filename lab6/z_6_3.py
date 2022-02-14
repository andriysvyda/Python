n = int(input('Введіть значення простору: '))
a = []
b = []
c = []
suma = []
for i in range(n):
    a.append(float(input('Input value {0} for vector a: '.format(i+1))))
    b.append(float(input('Input value {0} for vector b: '.format(i + 1))))
    c.append(float(input('Input value {0} for vector c: '.format(i + 1))))
    suma.append(a[i]-3*b[i]+2*c[i])
print (suma)
