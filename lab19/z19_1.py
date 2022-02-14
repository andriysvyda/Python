import random
import pickle


n = int(input("Кількість чисел = "))
a = [random.randint(-10, 10) for i in range(n)]
with open("file.txt", 'wb') as f:
    pickle.dump(a, f)
with open("file.txt", "rb") as f:
    b = pickle.load(f)
print(b)
sum_par = 0
for el in b:
    if el % 2 == 0:
        sum_par += 1
print("Кількість чисел = {0}".format(sum_par))

