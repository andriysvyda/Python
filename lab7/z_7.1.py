import random

n = int(input("рядки : "))
m = int(input("стовпці : "))
sum = 0
a = [[random.randrange(-100, 100) for j in range(m)] for i in range(n)]
print(*a, sep="\n")
for i in range(len(a)):
    for j in range(len(a)):
        if i%2 == 0 and j%2 == 0:
            if a[i][j] < 0:
                sum += 1
print(sum)
