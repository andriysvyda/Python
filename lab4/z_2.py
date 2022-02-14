#4  Дано цілі число  . Визначити, чи належить   множині  .
a = int(input("Перше число: "))
b = int(input("Друге число: "))
c = int(input("Третє число: "))
d = 1
d = d+1
if 3<=a<=9 and a in range(b,c):
    while b<c:
        b=b+d
    print("Належить")
else:
    print("Не належить")
