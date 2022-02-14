from random import randint
n, m = 3, 3
a =[[randint(10, 99) for j in range(m)] for i in range(n)]
for r in a:
    x, y = [], []
for i in range(n):
    for j in range(m):
        if i == j:
            x.append(a[i][j])
        elif j == m - 1 - i:
            y.append(a[i][j])
x = sorted(x)
y = sorted(y)
print()
for i in range(n):
    for j in range(m):
        if i == j:
            a[i][j] = min(x)
            x.remove(min(x))
        elif  j == m - 1 - i:
            a[i][j] = min(y)
            y.remove(min(y))
for r in a:
    print(' '.join([str(el) for el in r]))
