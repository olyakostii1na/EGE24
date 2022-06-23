def m(a):
    return a[0] * a[1] * a[2] * a[3] * a[4]


n = 200000000
count = 0
min_del = 10 ** 10
while count < 5:
    n += 1
    a = []
    for i in range(2, n):
        if n % i == 0:
            a += [i]
            if len(a) == 5:
                break
    if len(a) == 5:
        if 0 < m(a) < n:
            print(m(a))
            count += 1

