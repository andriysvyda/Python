'''
Знайти кількість від’ємних елементів у векторі x є R**n , які розташовані після першого додатного.
'''
import random
x = []
b = False
sum = 0
n = int(input("кількість елементів: "))
for i in range(n):
    x.append(random.randint(-100,100))
print(x)
for i in x:
    if i > 0:
        b = True
    if i < 0 and b == True:
        sum += 1
print("кількість від’ємних елементів : {0}".format(sum))


