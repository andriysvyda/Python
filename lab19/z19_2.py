import random
import pickle

n = int(input("Кількість чисел = "))
a = [random.randint(-10, 10) for i in range(n)]
with open("file.txt", "wb") as f:
    pickle.dump(a, f)
with open("file.txt", "rb") as f:
    b = pickle.load(f)
print(b)
dod_el = 0
vid_el = 0
for el in b:
    if el > 0:
       dod_el += 1
    else:
        vid_el += 1
if dod_el > vid_el:
    print("додатніх більше")
else:
    print("від'ємних більше")
with open("d.dat", "wb") as f:
    pickle.dump(dod_el, f)
with open("v.dat", "wb") as f:
    pickle.dump(vid_el, f)
