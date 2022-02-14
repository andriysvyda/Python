from random import randint


<<<<<<< HEAD
def smoothing(array, x, y):
    n = len(array)
    m = len(array[0])
    s = 0
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i or j) and 0 <= x + i < n and 0 <= y + j < m:
                count += 1
                s += array[x + i][y + j]
    return s / count


n, m = 3, 4
a = [[randint(10, 99) for _ in range(m)] for _ in range(n)]
for row in a:
    print(*row)
print()

res = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        res[i][j] = smoothing(a, i, j)

for row in res:
    print(*row)
=======
while True:
    ans = input('Do you want to search {y/n} ? : ' )
    if ans == 'n':
        break
    taxi_title = input('Taxi for search: ')
    taxi_res = search_taxi(taxi_list, taxi_title)
    if len(taxi_res) > 0:
        print(taxi_res)
    else:
        print('No TAXI')
>>>>>>> e5e43decfb74d3c16c1f840580d5afb05d5f799e
