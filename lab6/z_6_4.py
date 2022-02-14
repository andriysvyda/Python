l=[1, 0, 3, 4, 5, 0, 3, 2, 0, 0]
for el in l:
    if el == 0:
        l.remove(el)
        l.append(el)
print('Елементи які рівні 0, були переміщені в кінець масиву: ',l)
