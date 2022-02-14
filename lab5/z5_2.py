while True:
    n = int(input('n = '))

    order = 1
    while n >= 10:
        n //= 10
        order += 1

    print('Порядок числа =', order)
    print()