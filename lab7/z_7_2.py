import random

n = int(input("рядки : "))
m = int(input("стовпці : "))
sum = 0
a = [[(1/(i+j)) for j in range(1,m)] for i in range(1,n)]
print(*a, sep="\n")
for i in range(len(a)):
    for j in range(len(a)):
        if (i+j)%2 == 1:
            sum += a[i][j]
print(sum)
